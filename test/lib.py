import logging


def validate_response(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        assert (res.code == 0)
        if res.code != 0:
            logging.error(f'{func__name__} errors with {res}')
        return res

    return inner
