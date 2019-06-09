import base64
import json
import logging

import base58

from forge_sdk import protos as protos
from forge_sdk import utils as utils

logger = logging.getLogger('did-mobile')


class WalletResponse:
    def __init__(self, response):
        self.response = response
        self.user_info = response.get('userInfo')
        self.decoded_info = self.decode_user_info()
        self.requested_claim = self.decoded_info.get('requestedClaims')[0]

    def get_user_pk(self):
        pk = self.response.get('userPk')
        logger.debug("Got userpk from wallet {}".format(pk))
        return utils.multibase_b58decode(pk)

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

    def get_address(self):
        did = self.decoded_info.get('iss')
        logger.debug("Wallet Response:raw address: {}".format(did))
        did = str(did)
        return did.split(':')[-1]

    def get_did(self):
        return self.decoded_info.get('iss')

    def get_origin_tx(self):
        origin = self.requested_claim.get('origin')
        origin = str(origin)
        logger.debug(
            "Wallet Response:origin tx before decode: {}".format(origin),
        )
        decoded = base58.b58decode(origin[1:])
        tx = protos.Transaction()
        tx.ParseFromString(decoded)
        logger.debug(
            "Wallet Response:origin tx after base58 decode: {}".format(tx),
        )
        return tx

    def get_signature(self):
        sig = self.requested_claim.get('sig')
        logger.debug("Wallet Response:raw sig {}: ".format(sig))
        str_sig = str(sig)
        decoded_sig = base58.b58decode(str_sig[1:])
        logger.debug(
            "Wallet Response:sig after base58 decode: {}".format(
                decoded_sig),
        )
        return decoded_sig

    def get_asset_address(self):
        asset_address = self.requested_claim.get('did')
        if not asset_address:
            return None
        else:
            asset_address = str(asset_address)
            logger.debug(
                "Wallet Response: asset_address: {}".format(asset_address),
            )
            return asset_address
