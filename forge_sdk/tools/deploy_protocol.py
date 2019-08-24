import json
from forge_sdk import ForgeConn,did, mcrypto, protos, utils
import os.path
import sys
import logging

logger = logging.getLogger('tools-deploy')


def get_moderator_wallet():
    m_sk = os.environ.get('MODERATOR_SK')
    m_pk = os.environ.get('MODERATOR_PK')
    m_address = os.environ.get('MODERATOR_ADDR')

    if not m_sk or not m_pk or not m_address:
        logger.error('Fail to get MODERATOR_SK, MODERATOR_PK, MODERATOR_ADDR from environtment.')
        return
    m_wallet = protos.WalletInfo(
            sk=utils.multibase_b64decode(m_sk),
            pk=utils.multibase_b64decode(m_pk),
            address=m_address
    )
    return m_wallet


def delcare_moderator(forge):
    m_wallet = get_moderator_wallet()

    res = forge.rpc.declare(moniker='moderator',
                            wallet=m_wallet)

    if res.code == 0:
        logger.info("Moderator wallet declared!")
        return m_wallet
    else:
        logger.error("Fail to declare moderator wallet.")


def deploy(forge, input_file):
    m_wallet = get_moderator_wallet()
    with open(input_file) as f:
        raw = list(json.load(f).values())[0]
        logger.info("Protocol json loaded!")

        decoded = utils.multibase_b64decode(raw)
        itx = utils.parse_to_proto(decoded, protos.DeployProtocolTx)
        itx_hash = mcrypto.Hasher('sha3').hash(itx.SerializeToString())
        addr = did.AbtDid(role_type='tx', form='short').hash_to_did(itx_hash)
        itx.address = addr

        res = forge.rpc.send_itx(tx=itx,
                                 wallet=m_wallet,
                                 type_url='fg:t:deploy_protocol',
                                 nonce=0)
        if res.code == 0:
            logger.info("Successfully deployed new transaction protocol.")
        else:
            logger.error("Fail to deploy new transaction protocol.")
            logger.error(res)

if __name__=="__main__":
    file = sys.argv[1]
    grpc_socket = sys.argv[2]
    declare = sys.argv[3]

    forge = ForgeConn(grpc_socket)
    if delcare_moderator:
        delcare_moderator(forge)
    deploy(forge, file)

    #python forge_sdk/tools/deploy_protocol.py "/Users/shi/projects/Arcblock/forge-python-sdk/test/protocols/ticket/testTicket/testTicket.itx.json" 127.0.0.1:27210 True

