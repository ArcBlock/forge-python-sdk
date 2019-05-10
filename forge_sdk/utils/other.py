import logging

logger = logging.getLogger('forge-util')


def is_response_ok(response):
    if not response:
        logger.error('Response is None.')
        return False
    elif response.code == 0:
        return True
    else:
        logger.error(f'Response is not ok: {response}')
