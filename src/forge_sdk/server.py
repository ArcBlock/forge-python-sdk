import logging
import os
from socket import AF_INET
from socket import AF_UNIX
from socket import SOCK_STREAM
from socket import socket

import utils
from google.protobuf.internal.decoder import _DecodeVarint32

import protos
from .helper import SupportedActions


class ForgeServer:
    def __init__(
            self, handlers, address,
            buf_size=1500,
    ):
        self.server, self.address = ForgeServer.__parse_socket_address(address)
        self.buf_size = buf_size
        self.handlers = {handler.tx_type: handler for handler in handlers}
        self.buffer = b''
        self.active = True
        self.conn = None
        self.response_type = {
            SupportedActions.VERIFY_TX: protos.ResponseVerifyTx,
            SupportedActions.UPDATE_STATE: protos.ResponseUpdateState,
        }

        self.logger = logging.getLogger(__name__)
        self.logger.info('Forge server is initiated')

    def register_handler(self, handler):
        if SupportedActions.has_action(handler.tx_type):
            self.handlers[handler.tx_type] = handler
        else:
            raise ValueError('Transaction type is not supported!')

    def start(self):
        self.server.bind(self.address)
        self.server.listen(1)
        self.logger.info("socket type is : {}".format(self.server))
        self.logger.info(
            "server has binded to address {}".format(self.address),
        )
        while self.active:
            self.logger.info("Waiting for connection...")
            self.conn, addr = self.server.accept()
            self.logger.info("Connected!")

            while True:
                data = self.conn.recv(self.buf_size)
                if data:
                    self.buffer = self.buffer + data
                    self.__process_buffer()
                else:
                    break

    def __process_buffer(self):
        while self.__buffer_contains_full_request():
            request_bytes, len, pos = utils.decode_varint_request(
                self.buffer, 0,
            )
            request = utils.parse_proto_from(request_bytes, protos.Request)
            self.logger.info("request parsed: {}".format(request))
            action = request.WhichOneof('value')
            self.__handle_request(request, action)
            self.__update_buffer(pos, len)

    def __update_buffer(self, start, length):
        self.buffer = self.buffer[start + length:]

    def __handle_request(self, request, action):
        self.logger.info("Received a {} request!".format(action))
        action_request = getattr(request, action)
        itx_type = action_request.tx.itx.type_url
        if self.__is_type_supported(itx_type):
            func = self.__get_itx_action(itx_type, action)
            self.conn.send(
                self.__reply(result=func(action_request), action=action),
            )
        else:
            self.conn.send(self.__reply(action=action, unsupported=True))

        self.logger.info("type {} has been processed!".format(action))

    def __is_type_supported(self, itx_type):
        return itx_type in self.handlers.keys()

    def __get_itx_action(self, itx_type, action):
        return getattr(self.handlers.get(itx_type), action)

    def stop(self):
        self.active = False

    @staticmethod
    def __parse_socket_address(address):
        socket_type = address.split('://')[0]
        socket_addr = address.split('://')[1]

        if socket_type == 'tcp':
            parsed_addr = socket_addr.split(":")
            return socket(AF_INET, SOCK_STREAM), (
                parsed_addr[0], int(parsed_addr[1]),
            )
        elif socket_type == 'unix':
            os.unlink(socket_addr)
            return socket(AF_UNIX, SOCK_STREAM), socket_addr
        else:
            raise AttributeError(
                "The socket in Forge.toml should start with either tcp "
                "or unix",
            )

    def __buffer_contains_full_request(self):
        if len(self.buffer) > 0:
            req_len, start_pos = _DecodeVarint32(self.buffer, 0)
            return req_len + start_pos <= len(self.buffer)
        else:
            return False

    def __reply(self, action, unsupported=False, result=None):
        if unsupported:
            result = protos.Response(
                **{action: self.response_type[action](
                    code=protos.StatusCode.UNSUPPORTED_TX,
                )}
            )

        else:
            result = protos.Response(**{action: result})
        return utils.encode_varint_request(result)
