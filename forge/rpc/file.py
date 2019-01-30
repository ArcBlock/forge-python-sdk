from forge import protos
from forge.utils import utils


class RpcFile:
    def __init__(self, chan):
        self.stub = protos.FileRpcStub(chan)

    def store_file(self, chunk=b'', req=None):
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
            return self.stub.store_file(utils.to_iter(to_req, req))
        else:
            chunks = utils.to_iter(to_req, chunk)
            return self.stub.store_file(chunks)

    def load_file(self, file_hash='', req=None):
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
            return self.stub.load_file(req)
        else:
            req_kwargs = {
                'hash': file_hash,
            }
            return self.stub.load_file(protos.RequestLoadFile(**req_kwargs))
