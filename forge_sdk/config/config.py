import logging

logger = logging.getLogger('forge-config')


class ForgeConfig:
    def __init__(self, parsed_file):
        self.file = parsed_file

    def __getattr__(self, item):
        forge = self.file.get('forge')
        token = self.file.get('forge').get('token')
        return self.file.get(item, forge.get(item, token.get(item)))
