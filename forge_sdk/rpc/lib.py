from collections import Iterable


def to_iter(to_req, data):
    if isinstance(data, dict) or isinstance(data, str):
        return iter([to_req(data)])
    elif isinstance(data, Iterable):
        return (to_req(i) for i in data)
    else:
        return iter([data])
