from forge import protos
from forge.config import config
from forge.utils import utils

stub = protos.FileRpcStub(config.get_grpc_channel())


def store_file(chunk=b'', req=None):
    """
    RPC call to store file

    Parameters
    ----------
    req: stream RequestStoreFile
    chunk: iterator of bytes

    Returns
    -------
    ResponseStoreFile

    """

    def to_req(item):
        if isinstance(item, protos.RequestStoreFile):
            return item
        else:
            return protos.RequestStoreFile(chunk=item)

    if req is not None:
        return stub.store_file(utils.to_iter(to_req, req))
    else:
        chunks = utils.to_iter(to_req, chunk)
        return stub.store_file(chunks)


def load_file(file_hash='', req=None):
    """
    RPC call to load file.

    Parameters
    ----------
    req: RequestLoadFile
    file_hash: string

    Returns
    -------
    stream ResponseLoadFile

    """
    if req is not None:
        return stub.load_file(req)
    else:
        req_kwargs = {
            'hash': file_hash,
        }
        return stub.load_file(protos.RequestLoadFile(**req_kwargs))
