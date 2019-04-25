import ast
import json
import logging

from event_chain.app import controllers
from event_chain.app import db
from event_chain.app import models
from event_chain.app import utils
from event_chain.config import config
from flask import Blueprint
from flask import request
from flask import Response
from flask import url_for

from forge_sdk.utils import utils as forge_utils

logger = logging.getLogger('api-mobile')

api_mobile = Blueprint(
    'api_mobile',
    __name__
)


@api_mobile.route(
    "/buy-ticket/<event_address>",
    methods=['GET', 'POST'],
)
def buy_ticket(event_address):
    try:
        error = utils.verify_event(event_address)
        if error:
            return error
        if request.method == 'GET':
            logger.debug("Receives get request for mobile-buy-ticket.")
            user_did = request.args.get('userDid')
            user_pk = forge_utils.multibase_b58decode(
                request.args.get('userPk'))
            if not user_did:
                return utils.response_error("Please provide a valid user did.")
            user_address = user_did.split(":")[2]
            logger.debug(
                "user address parsed from request {}".format(user_address),
            )

            event = models.get_event_state(event_address)
            updated_exchange_tx = utils.update_tx_multisig(
                event.get_exchange_tx(),
                user_address,
                user_pk
            )
            logger.debug('new tx {}:'.format(updated_exchange_tx))
            call_back_url = config.SERVER_ADDRESS + url_for(
                'api_mobile.buy_ticket', event_address=event_address)
            des = 'Confirm the purchase below.'

            did_request_params = {
                'user_did': user_did,
                'tx': updated_exchange_tx,
                'url': call_back_url,
                'description': des,
                'action': 'responseAuth',
                'workflow': 'buy-ticket',
            }
            response = controllers.require_sig(**did_request_params)
            logger.debug('did auth response: {}'.format(response))
            return response

        elif request.method == 'POST':
            logger.debug("Receives post request for mobile-buy-ticket.")
            try:
                req_data = request.get_data(as_text=True)
                logger.debug("Receives data from wallet {}".format(req_data))
                req = ast.literal_eval(req_data)
                wallet_response = models.WalletResponse(req)
            except Exception as e:
                logger.error(e, exc_info=True)
                return utils.response_error("Error in parsing wallet data.")

            user_address = wallet_response.get_address()
            participant_state = models.get_participant_state(user_address)
            if not participant_state:
                return utils.response_error(
                    "user {} doesn't exist.".format(user_address))

            ticket_address, hash = controllers.buy_ticket_mobile(
                event_address,
                user_address,
                wallet_response.get_signature(),
                wallet_response.get_user_pk(),
            )

            if ticket_address and hash:
                logger.info("Ticket {} is bought successfully "
                            "by mobile.".format(ticket_address))
                base58_encoded = utils.base58_encode_tx(
                    utils.update_tx_multisig(
                        models.get_event_state(
                            event_address).get_exchange_tx(),
                        user_address,
                        wallet_response.get_user_pk(),
                    ))
                js = json.dumps({'ticket': ticket_address,
                                 'hash': hash,
                                 'tx': base58_encoded})
                logger.debug('success response: {}'.format(str(js)))
                resp = Response(js, status=200, mimetype='application/json')
                return resp
            else:
                logger.error(
                    'Fail to buy ticket. ticket '
                    'address: {0}, hash : {1}.'.format(ticket_address,
                                                       hash))
                return utils.response_error(
                    'Please try buying the ticket again.')
    except Exception as e:
        logger.error(e, exc_info=True)
        return utils.response_error('Exception in buying ticket.')


@api_mobile.route("/error", methods=['GET', 'POST'])
def error():
    return "Sorry there's something wrong in purchasing your ticket."


@api_mobile.route(
    "/poke",
    methods=['GET', 'POST'],
)
def poke():
    try:
        if request.method == 'GET':
            logger.debug("Receives get request for mobile-poke.")
            user_did = request.args.get('userDid')
            user_pk = forge_utils.multibase_b58decode(
                request.args.get('userPk'))
            if not user_did:
                return utils.response_error("Please provide a valid user did.")
            user_address = user_did.split(":")[2]
            logger.debug(
                "user address parsed from request {}".format(user_address),
            )
            poke_tx = controllers.gen_poke_tx(user_address, user_pk)
            logger.debug('poke tx {}:'.format(poke_tx))
            call_back_url = config.SERVER_ADDRESS + url_for('api_mobile.poke')
            des = 'Poke and get reward.'

            did_request_params = {
                'user_did': user_did,
                'tx': poke_tx,
                'url': call_back_url,
                'description': des,
                'action': 'responseAuth',
                'workflow': 'poke',
            }
            response = controllers.require_sig(**did_request_params)
            logger.debug('did auth response: {}'.format(response))
            return response

        elif request.method == 'POST':
            logger.debug("Receives post request for mobile-poke.")
            try:
                req_data = request.get_data(as_text=True)
                logger.debug("Receives data from wallet {}".format(req_data))
                req = ast.literal_eval(req_data)
                wallet_response = models.WalletResponse(req)
            except Exception as e:
                logger.error(e, exc_info=True)
                return utils.response_error("Error in parsing wallet data.")
            user_sig = wallet_response.get_signature()
            poke_tx = wallet_response.get_origin_tx()
            hash = controllers.send_poke_tx(poke_tx, user_sig)
            if hash:
                js = json.dumps({'hash': hash,
                                 'tx': utils.base58_encode_tx(poke_tx)})
                logger.debug('success response: {}'.format(str(js)))
                resp = Response(js, status=200, mimetype='application/json')
                return resp
            else:
                return utils.response_error('Whoops! All rewards are taken.'
                                            ' Please try again tomorrow.')
    except Exception as e:
        logger.error(e, exc_info=True)
        return utils.response_error('Whoops! All rewards are taken.'
                                    ' Please try again tomorrow.')


@api_mobile.route(
    "/require-asset/<event_address>",
    methods=['GET', 'POST'],
)
def require_asset(event_address):
    try:
        error = utils.verify_event(event_address)
        if error:
            return error
        event = models.get_event_state(event_address)

        if request.method == 'GET':
            call_back_url = config.SERVER_ADDRESS + url_for(
                'api_mobile.require_asset', event_address=event_address)
            des = 'Select a ticket for event.'
            target = event.event_info.title
            did_request_params = {
                'url': call_back_url,
                'description': des,
                'action': 'responseAuth',
                'workflow': 'use-ticket',
                'target': target,
            }
            response = controllers.require_asset(**did_request_params)
            return response

        if request.method == 'POST':
            try:
                req_data = request.get_data(as_text=True)
                logger.debug("Receives data from wallet {}".format(req_data))
                req = ast.literal_eval(req_data)
                wallet_response = models.WalletResponse(req)
            except Exception as e:
                logger.error(
                    "error in parsing wallet data, error:{}".format(e),
                )
                logger.error(e, exc_info=True)
                return utils.response_error(
                    "Error in parsing wallet data. Original "
                    "data received is {}".format(req))

            asset_address = wallet_response.get_asset_address()
            if not asset_address:
                logger.error(
                    "No available asset address in wallet response.",
                )
                return utils.response_error("Please provide an asset address.")

            error = utils.verify_ticket(asset_address)
            if error:
                logger.error(
                    "ticket address in wallet response is not valid.",
                )
                return utils.response_error(
                    "Please provide a valid ticket address.")

            user_address = wallet_response.get_address()
            call_back_url = config.SERVER_ADDRESS + \
                url_for('api_mobile.consume', ticket_address=asset_address)
            des = 'Confirm to use the ticket.'
            consume_tx = event.event_info.consume_tx
            multisig_data = forge_utils.encode_to_any(
                'fg:x:address',
                asset_address,
            )

            new_tx = utils.update_tx_multisig(
                tx=consume_tx, signer=user_address,
                pk=wallet_response.get_user_pk(),
                data=multisig_data,
            )

            did_request_params = {
                'user_did': user_address,
                'tx': new_tx,
                'url': call_back_url,
                'description': des,
                'action': 'responseAuth',
                'workflow': 'use-ticket',
            }
            response = controllers.require_sig(**did_request_params)
            return response

    except Exception as e:
        logger.error(e, exc_info=True)
        return utils.response_error("Exception in requesting asset.")


@api_mobile.route(
    "/consume/<ticket_address>", methods=['POST'],
)
def consume(ticket_address):
    try:
        error = utils.verify_ticket(ticket_address)
        if error:
            return error

        ticket = models.get_ticket_state(ticket_address)
        event = models.get_event_state(ticket.event_address)

        if request.method == 'POST':
            try:
                req_data = request.get_data(as_text=True)
                logger.debug("Receives data from wallet {}".format(req_data))
                req = ast.literal_eval(req_data)
                wallet_response = models.WalletResponse(req)
            except Exception as e:
                logger.error(e, exc_info=True)
                return utils.response_error(
                    "Error in parsing wallet data. Original "
                    "data received is {}".format(req))

            hash = controllers.consume_ticket_mobile(
                ticket,
                event.event_info.consume_tx,
                wallet_response.get_address(),
                wallet_response.get_signature(),
                wallet_response.get_user_pk(),
            )
            multisig_data = forge_utils.encode_to_any(
                'fg:x:address',
                ticket_address,
            )
            base58_tx = utils.base58_encode_tx(utils.update_tx_multisig(
                tx=event.event_info.consume_tx,
                signer=wallet_response.get_address(),
                pk=wallet_response.get_user_pk(),
                data=multisig_data
            ))
            if hash:
                logger.info("ConsumeTx has been sent.")
                js = json.dumps({'hash': hash,
                                 'tx': base58_tx})
                logger.debug('success response: {}'.format(js))
                resp = Response(js, status=200, mimetype='application/json')
                return resp
            else:
                logger.error('Fail to consume ticket.')
                return utils.response_error('Your ticket might have been '
                                            'checked out before. '
                                            'Please wait and try again.')
    except Exception as e:
        logger.error(e, exc_info=True)
        return utils.response_error("Exception in consuming ticket.")
