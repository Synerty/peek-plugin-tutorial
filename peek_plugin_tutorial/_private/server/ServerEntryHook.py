import logging

from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC

from peek_plugin_tutorial._private.storage import DeclarativeBase, loadStorageTuples
from peek_plugin_base.server.PluginServerStorageEntryHookABC import PluginServerStorageEntryHookABC

from peek_plugin_tutorial._private.tuples import loadPrivateTuples
from peek_plugin_tutorial.tuples import loadPublicTuples

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

    @property
    def dbMetadata(self):
        return DeclarativeBase.metadata

    def start(self):
        """ Load

        This will be called when the plugin is loaded, just after the db is migrated.
        Place any custom initialiastion steps here.

        """

        session = self.dbSessionCreator()

        # This will retrieve all the settings
        from peek_plugin_tutorial._private.storage.Setting import globalSetting
        allSettings = globalSetting(session)
        logger.debug(allSettings)

        # This will retrieve the value of property1
        from peek_plugin_tutorial._private.storage.Setting import PROPERTY1
        value1 = globalSetting(session, key=PROPERTY1)
        logger.debug("value1 = %s" % value1)

        # This will set property1
        globalSetting(session, key=PROPERTY1, value="new value 1")
        session.commit()

        session.close()

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
