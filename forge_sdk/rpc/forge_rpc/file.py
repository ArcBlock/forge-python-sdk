from forge_sdk.protos import protos
from forge_sdk.rpc import lib


class ForgeFileRpc:

    def __init__(self, channel):
        self.stub = protos.FileRpcStub(channel)

    def store_file(self, chunk):
        """GRPC call to store file

        Args:
            chunk(bytes or list[bytes]): file bytes to store

        Returns:
            ResponseStoreFile

        """

        def to_req(item):
            return protos.RequestStoreFile(chunk=item)

        requests = lib.to_iter(to_req, chunk)
        return self.stub.store_file(requests)

    def load_file(self, file_hash):
        """GRPC call to load stored file

        Args:
            file_hash(string): hash of stored file

        Returns:
            ResponseLoadFile(stream)

        """

        req_kwargs = {
            'hash': file_hash,
        }
        request = protos.RequestLoadFile(**req_kwargs)
        return self.stub.load_file(request)

    def pin_file(self, file_hash):
        """GRPC call to pin file so Forge will keep the file

        Args:
            file_hash(string): hash of the file to pin

        Returns:
            ResponsePinFile

        """
        request = protos.RequestPinFile(hash=file_hash)
        return self.stub.pin_file(request)
