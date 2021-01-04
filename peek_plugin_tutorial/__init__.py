__version__ = "0.0.0"

from peek_plugin_base.server.PluginLogicEntryHookABC import PluginLogicEntryHookABC

from peek_plugin_base.client.PluginClientEntryHookABC import PluginClientEntryHookABC

from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC

from peek_plugin_base.worker.PluginWorkerEntryHookABC import PluginWorkerEntryHookABC

from typing import Type


def peekLogicEntryHook() -> Type[PluginLogicEntryHookABC]:
    from ._private.server.LogicEntryHook import LogicEntryHook

    return LogicEntryHook


def peekOfficeEntryHook() -> Type[PluginClientEntryHookABC]:
    from ._private.client.ClientEntryHook import ClientEntryHook

    return ClientEntryHook


def peekFieldEntryHook() -> Type[PluginClientEntryHookABC]:
    from ._private.client.ClientEntryHook import ClientEntryHook

    return ClientEntryHook


def peekAgentEntryHook() -> Type[PluginAgentEntryHookABC]:
    from ._private.agent.AgentEntryHook import AgentEntryHook

    return AgentEntryHook


def peekWorkerEntryHook() -> Type[PluginWorkerEntryHookABC]:
    from ._private.worker.WorkerEntryHook import WorkerEntryHook

    return WorkerEntryHook
