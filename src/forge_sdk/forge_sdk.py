from rpc import ForgeRpc
from config import parser


class ForgeSdk:
	def __init__(self, config_path=None):
		if config_path:
			self.config = parser.parse_from_path(config_path)
		else:
			self.config = parser.parse_from_default()
		self.rpc = ForgeRpc(self.config.socket_target)


