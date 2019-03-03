import base64
import json
import logging

from enum import Enum
from google.protobuf.timestamp_pb2 import Timestamp

import forge.utils as forge_utils
from . import protos

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

    def decode_user_info(self):
        if not self.user_info:
            logger.error(
                "Fail to parse user_info from this Response {}.".format(
                    self.response,
                ),
            )
        else:
            sig = self.user_info.split('.')[1]
            decoded = base64.decodebytes(
                (sig + '=' * (-len(sig) % 4)).encode(),
            ).decode()
            dict = json.loads(decoded)
            logger.debug("User info is decoded successfully. {}".format(dict))
            return dict

    def get_address(self):
        did = self.decoded_info.get('iss')
        logger.debug("Parsed wallet address successfully!: {}".format(did))
        return did.split(':')[-1]

    def get_signature(self):
        sig = self.requested_claim.get('sig')
        logger.debug("Parsed wallet signature successfully! {}".format(sig))
        return sig

    def get_event_address(self):
        tx = self.requested_claim.get('tx')
        decoded_tx = base64.decodebytes((tx + '=' * (-len(tx) % 4)).encode())

        parsed_tx = protos.Transaction()
        parsed_tx.ParseFromString(decoded_tx)
        logger.debug("Parsed tx successfully! {}".format(parsed_tx))
        exchange_itx = forge_utils.parse_to_proto(
            parsed_tx.itx.value,
            protos.ExchangeTx,
        )
        event_address = exchange_itx.data.value.decode()
        return event_address


def add_multi_sig_to_tx(tx, address, signature):
    new_tx = protos.Transaction()
    new_tx.CopyFrom(tx)
    kv_pair = protos.vendor.KVPair(
        key=address.encode(),
        value=signature.encode(),
    )
    new_tx.__setattr__('signatures', kv_pair)
    return new_tx


class ForgeTxType(Enum):
    ACTIVATE_ASSET = 'fg:t:activate_asset'
    CREATE_ASSET = 'fg:t:create_asset'
    EXCHANGE = 'fg:t:exchange'
