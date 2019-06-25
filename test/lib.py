import logging


def validate_response(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if res.code != 0:
            logging.error(f'{func.__name__} errors with {res}')
        assert (res.code == 0)
        return res

    return inner
