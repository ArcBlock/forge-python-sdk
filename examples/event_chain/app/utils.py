import json
import logging
from enum import Enum
from time import sleep

import base58
import event_chain.protos as protos
import requests
from event_chain.config.config import APP_ADDR
from event_chain.config.config import APP_PK
from event_chain.config.config import APP_SK
from event_chain.config.config import ARC
from flask import flash
from flask import Response
from flask import session
from google.protobuf.any_pb2 import Any
from google.protobuf.timestamp_pb2 import Timestamp

from forge_sdk.utils import utils as forge_utils

logger = logging.getLogger('ec-utils')


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                "Error in the {} field - {}".format(
                    getattr(form, field).label.text,
                    error), 'error',
            )


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def verify_ticket(address):
    from event_chain.app.controllers import ticket
    if not address:
        return response_error("Please provide a valid ticket address.")
    try:
        ticket.verify_ticket_address(address)
    except Exception as e:
        return response_error(e.args[0])


def verify_event(address):
    from event_chain.app.controllers import event
    if not address:
        return response_error("Please provide a valid event address.")
    try:
        event.verify_event_address(address)
    except Exception as e:
        return response_error(e.args[0])


def response_error(msg):
    error = json.dumps({'error': msg})
    return Response(error, status=400, mimetype='application/json')


def wait():
    sleep(5)


def refresh_token():
    from event_chain.app.controllers import admin
    user = session.get('user')
    user = admin.load_user(
        moniker=user.moniker,
        passphrase=user.passphrase,
        address=user.address,
    )
    session['user'] = user
    logger.info("Token refreshed!")


def gen_did_url(url, action):
    params = {
        'appPk': APP_PK,
        'appDid': 'did:abt:' + APP_ADDR,
        'action': action,
        'url': url,
    }
    r = requests.Request('GET', ARC, params=params).prepare()
    logger.debug(
        "callback url for DID call. {}".format(
            url,
        ),
    )
    return r.url


def send_did_request(
        url, description, endpoint, workflow, tx=None,
        target=None,
):
    if tx:
        base58_encoded = (b'z' + base58.b58encode(
            tx.SerializeToString(),
        )).decode()
        g.logger.debug(
            u"Sending request to DID with base58 encoded tx: {} and"
            u" url {}".format(base58_encoded, url),
        )
    else:
        base58_encoded = None

    params = {
        'sk': APP_SK,
        'pk': APP_PK,
        'address': APP_ADDR,
        'tx': base58_encoded,
        'description': description,
        'target': target,
        'url': url,
        'workflow': workflow,
    }
    headers = {'content-type': 'application/json'}
    call_url = 'http://localhost:4000/api/' + endpoint
    logger.debug('call url : {}'.format(call_url))
    response = requests.post(
        call_url,
        json=params,
        headers=headers,
    )
    logger.info("Response from did: {}".format(response.content.decode()))
    return Response(
        response.content.decode(), status=200,
        mimetype='application/json',
    )


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


def add_multi_sig_to_tx(tx, address, signature, user_pk):
    logger.debug("Adding multisig to tx...")
    logger.debug("tx: {}".format(tx))
    logger.debug("address: {}".format(address))
    logger.debug("signature: {}".format(signature))
    new_tx = update_tx_multisig(tx, address, user_pk, signature)
    logger.debug("Address and signature has been added to tx: ")
    logger.debug("new tx: {}".format(new_tx))

    return new_tx


def to_display_time(timestamp):
    dt = timestamp.ToDatetime()
    return dt.strftime("%a, %b %d, %Y")


def to_short_time(time):
    dt = time.ToDatetime()
    return dt.strftime("%Y/%m/%d")


def shorten_hash(data):
    head = data[0:6]
    tail = data[-4:]
    return head + "..." + tail


def time_diff(t1, t2):
    return t2.ToDatetime() - t1.ToDatetime()


def update_tx_multisig(tx, signer, pk, signature=None, data=None):
    multisig = protos.Multisig(
        signer=signer,
        signature=signature,
        data=data,
        pk=pk,
    )
    params = {
        'from': getattr(tx, 'from'),
        'nonce': tx.nonce,
        'signature': tx.signature,
        'chain_id': tx.chain_id,
        'signatures': [multisig],
        'itx': tx.itx,
        'pk': tx.pk,
    }
    new_tx = protos.Transaction(**params)
    return new_tx


def update_tx_signature(tx, signature):
    params = {
        'from': getattr(tx, 'from'),
        'nonce': tx.nonce,
        'signature': signature,
        'chain_id': tx.chain_id,
        'signatures': tx.signatures,
        'itx': tx.itx,
        'pk': tx.pk,
    }
    new_tx = protos.Transaction(**params)
    return new_tx


def base58_encode_tx(tx):
    b = tx.SerializeToString()
    return forge_utils.multibase_b58encode(b)


class ForgeTxType(Enum):
    ACTIVATE_ASSET = 'fg:t:activate_asset'
    CREATE_ASSET = 'fg:t:create_asset'
    EXCHANGE = 'fg:t:exchange'


def insert_to_sql(db, data):
    db.session.add(data)
    db.session.commit()
