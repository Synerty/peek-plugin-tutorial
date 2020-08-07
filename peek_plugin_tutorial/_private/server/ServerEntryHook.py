import logging

from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC
from peek_plugin_tutorial._private.storage import DeclarativeBase
from peek_plugin_tutorial._private.storage.DeclarativeBase import loadStorageTuples
from peek_plugin_base.server.PluginServerStorageEntryHookABC import PluginServerStorageEntryHookABC
from peek_plugin_tutorial._private.tuples import loadPrivateTuples
from peek_plugin_tutorial.tuples import loadPublicTuples
from .admin_backend import makeAdminBackendHandlers
from .tuple_providers.TupleDataObservable import makeTupleDataObservableHandler

logger = logging.getLogger(__name__)


class ServerEntryHook(PluginServerEntryHookABC, PluginServerStorageEntryHookABC):
    def __init__(self, *args, **kwargs):
        """" Constructor """
        # Call the base classes constructor
        PluginServerEntryHookABC.__init__(self, *args, **kwargs)

        #: Loaded Objects, This is a list of all objects created when we start
        self._loadedObjects = []

    def load(self) -> None:
        """ Load

        This will be called when the plugin is loaded, just after the db is migrated.
        Place any custom initialiastion steps here.

        """
        loadStorageTuples()
        loadPrivateTuples()
        loadPublicTuples()
        logger.debug("Loaded")

    def start(self):
        """ Start

        This will be called to start the plugin.
        Start, means what ever we choose to do here. This includes:

        -   Create Controllers

        -   Create payload, observable and tuple action handlers.

        """
        tupleObservable = makeTupleDataObservableHandler(self.dbSessionCreator)
        self._loadedObjects.extend(makeAdminBackendHandlers(tupleObservable, self.dbSessionCreator))
        self._loadedObjects.append(tupleObservable)
        logger.debug("Started")

    def stop(self):
        """ Stop

        This method is called by the platform to tell the peek app to shutdown and stop
        everything it's doing
        """
        # Shutdown and dereference all objects we constructed when we started
        while self._loadedObjects:
            self._loadedObjects.pop().shutdown()

        logger.debug("Stopped")

    def unload(self):
        """Unload

        This method is called after stop is called, to unload any last resources
        before the PLUGIN is unlinked from the platform

        """
        logger.debug("Unloaded")

    @property
    def dbMetadata(self):
        return DeclarativeBase.metadata

