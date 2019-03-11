import base64
import codecs
import json
import logging
import math

import base58
import event_chain.protos as protos
from enum import Enum
from event_chain.application import app
from google.protobuf.any_pb2 import Any
from google.protobuf.timestamp_pb2 import Timestamp

logger = logging.getLogger('ec-helpers')


def gen_timestamp(datetime):
    res = Timestamp()
    res.FromDatetime(datetime)
    return res


def add_to_proto_list(info, repeated):
    res = {item for item in repeated}
    res.add(info)
    return res


def remove_from_proto_list(info, repeated):
    res = filter(lambda item: item != info, repeated)
    return res


class WalletResponse:
    def __init__(self, response):
        self.response = response
        self.user_info = response.get('userInfo')
        self.decoded_info = self.decode_user_info()
        self.requested_claim = self.decoded_info.get('requestedClaims')[0]
        self.get_origin_tx()

    def decode_user_info(self):
        if not self.user_info:
            logger.error(
                "Fail to parse user_info from this Response {}.".format(
                    self.response,
                ),
            )
        else:
            sig = self.user_info.split('.')[1]
            decoded = base64.urlsafe_b64decode(
                (sig + '=' * (-len(sig) % 4)).encode(),
            ).decode()
            dict = json.loads(decoded)
            logger.debug("User info is decoded successfully. {}".format(dict))
            return dict

    def get_origin_tx(self):
        origin = self.requested_claim.get('origin')
        origin = str(origin)
        logger.debug("Origin tx before decode: {}".format(origin))
        decoded = base58.b58decode(origin[1:])
        tx = protos.Transaction()
        tx.ParseFromString(decoded)
        logger.debug("Origin tx after base58 decode: {}".format(tx))

    def get_address(self):
        did = self.decoded_info.get('iss')
        logger.debug("Parsed did type {}".format(type(did)))
        logger.debug("Parsed did: {}".format(did))
        did = str(did)
        return did.split(':')[-1]

    def get_signature(self):
        sig = self.requested_claim.get('sig')
        logger.debug("Parsed sig type {}".format(type(sig)))
        logger.debug("Parsed sig {}: ".format(sig))
        str_sig = str(sig)
        decoded_sig = base58.b58decode(str_sig[1:])
        logger.debug("sig after base58 decode: {}".format(decoded_sig))
        return decoded_sig

    # def get_event_address(self):
    #     tx = self.requested_claim.get('tx')
    #     decoded_tx = base64.urlsafe_b64decode(
    #             (tx + '=' * (-len(tx) % 4)).encode('utf8'))
    #
    #     parsed_tx = protos.Transaction()
    #     parsed_tx.ParseFromString(decoded_tx)
    #     logger.debug("Parsed tx successfully! {}".format(parsed_tx))
    #     exchange_itx = forge_utils.parse_to_proto(
    #             parsed_tx.itx.value,
    #             protos.ExchangeTx,
    #     )
    #     event_address = exchange_itx.data.value.decode('utf8')
    #     return event_address


def add_multi_sig_to_tx(tx, address, signature):
    logger.debug("Adding multisig to tx...")
    logger.debug("tx: {}".format(tx))
    logger.debug("address: {}".format(address))
    logger.debug("signature: {}".format(signature))
    # #
    # # parsed_address = tx.signatures[0].signer
    # # assert (address == parsed_address)
    # multisig = protos.Multisig(
    #     signer=address,
    #     signature=signature,
    # )
    # parmas = {
    #     'from': getattr(tx, 'from'),
    #     'nonce': tx.nonce,
    #     'signature': tx.signature,
    #     'chain_id': tx.chain_id,
    #     'signatures': [multisig],
    #     'itx': tx.itx,
    # }
    new_tx = update_tx_multisig(tx, address, signature)
    logger.debug("Address and signature has been added to tx: ")
    logger.debug("new tx: {}".format(new_tx))

    return new_tx


def to_display_time(timestamp):
    dt = timestamp.ToDatetime()
    return dt.strftime("%Y/%m/%d")


def update_tx_multisig(tx, signer, signature='', data=None):
    multisig = protos.Multisig(
        signer=signer,
        signature=signature,
        data=data,
    )
    params = {
        'from': getattr(tx, 'from'),
        'nonce': tx.nonce,
        'signature': tx.signature,
        'chain_id': tx.chain_id,
        'signatures': [multisig],
        'itx': tx.itx,
    }
    new_tx = protos.Transaction(**params)
    return new_tx


def encode_string_to_any(type_url, str):
    return Any(
        type_url=type_url,
        value=str.encode(),
    )


def is_event_address_valid(event_address):
    event = app.get_event_state(event_address)
    if not event:
        logger.error(u'Event {} does not exist.'.format(event_address))
        return False
    user = app.get_participant_state(event.owner)
    if not user:
        logger.error(u'User {} does not exist.'.format(event.owner))
        return False
    return True


def is_ticket_address_valid(ticket_address):
    ticket = app.get_ticket_state(ticket_address)
    if not ticket:
        logger.error(u'Ticket {} does not exist.'.format(ticket_address))
        return False
    return is_event_address_valid(ticket.event_address)


class ForgeTxType(Enum):
    ACTIVATE_ASSET = 'fg:t:activate_asset'
    CREATE_ASSET = 'fg:t:create_asset'
    EXCHANGE = 'fg:t:exchange'
