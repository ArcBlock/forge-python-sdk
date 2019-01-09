import os
from os.path import expanduser
import toml

def parse_forge_toml():
    #get from env

    #get from .forge/forge.toml

    #get from cwd!(), "forge.toml"
    forge_toml = toml.load('/Users/shi/.forge/forge.toml')
    forge_sock_grpc = forge_toml['forge']['sock_grpc']
    user_home = expanduser('~')
    sock_target = '/'.join(["unix:/",user_home, ".forge/core",forge_sock_grpc.split("//")[1]])
    return sock_target
