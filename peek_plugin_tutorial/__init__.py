__version__ = '0.0.0'

from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC
from typing import Type

def peekServerEntryHook() -> Type[PluginServerEntryHookABC]:
    from ._private.server.ServerEntryHook import ServerEntryHook
    return ServerEntryHook

from peek_plugin_base.client.PluginClientEntryHookABC import PluginClientEntryHookABC
from typing import Type


def peekClientEntryHook() -> Type[PluginClientEntryHookABC]:
    from ._private.client.ClientEntryHook import ClientEntryHook
    return ClientEntryHook

from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC
from typing import Type


def peekAgentEntryHook() -> Type[PluginAgentEntryHookABC]:
    from ._private.agent.AgentEntryHook import AgentEntryHook
    return AgentEntryHook

