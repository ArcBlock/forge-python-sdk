from forge import protos
from forge.config import config
from forge.utils import utils

stub = protos.FileRpcStub(config.get_grpc_channel())


def store_file(chunk, req=None):
    """GRPC call to store file

    Args:
        chunk(bytes or list[bytes]): file bytes to store
        req(:obj:`RequestStoreFile`): stream of completed request

    Returns:
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


def load_file(file_hash, req=None):
    """GRPC call to load stored file

    Args:
        file_hash(string): hash of stored file
        req(:obj:`RequestLoadFile`): completed request

    Returns:
        ResponseLoadFile(stream)

    """

    if req is not None:
        return stub.load_file(req)
    else:
        req_kwargs = {
            'hash': file_hash,
        }
        return stub.load_file(protos.RequestLoadFile(**req_kwargs))


def pin_file(file_hash, req=None):
    """GRPC call to pin file so Forge will keep the file

    Args:
        file_hash(string): hash of the file to pin
        req(:obj:`ReqeustPinFile`): completedRequest

    Returns:
        ResponsePinFile

    """
    if req:
        return stub.pin_file(req)
    else:
        return stub.pin_file(protos.RequestPinFile(hash=file_hash))
