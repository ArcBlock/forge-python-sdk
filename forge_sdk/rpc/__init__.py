import logging
from inspect import getmembers
from inspect import isfunction

from forge_sdk.rpc import helper
from forge_sdk.rpc.forge_rpc import chain as chain_rpc
from forge_sdk.rpc.forge_rpc import event as event_rpc
from forge_sdk.rpc.forge_rpc import file as file_rpc
from forge_sdk.rpc.forge_rpc import state as state_rpc
from forge_sdk.rpc.forge_rpc import statistic as stats_rpc
from forge_sdk.rpc.forge_rpc import wallet as wallet_rpc

logger = logging.getLogger('forge-rpc')


def __get_module_functions(module):
    return {item[0]: getattr(module, item[0]) for item in
            getmembers(module, isfunction)}


__all_services = {**__get_module_functions(chain_rpc),
                  **__get_module_functions(state_rpc),
                  **__get_module_functions(event_rpc),
                  **__get_module_functions(file_rpc),
                  **__get_module_functions(wallet_rpc),
                  **__get_module_functions(stats_rpc),
                  **__get_module_functions(helper),
                  }

for name, func in __all_services.items():
    if not name.startswith('__'):
        vars()[name] = func
