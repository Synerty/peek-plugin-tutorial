import logging

from peek_plugin_base.worker.PluginWorkerEntryHookABC import PluginWorkerEntryHookABC
from peek_plugin_tutorial._private.worker.tasks import RandomNumber
logger = logging.getLogger(__name__)


class WorkerEntryHook(PluginWorkerEntryHookABC):
    def __init__(self, *args, **kwargs):
        """" Constructor """
        # Call the base classes constructor
        PluginWorkerEntryHookABC.__init__(self, *args, **kwargs)

        #: Loaded Objects, This is a list of all objects created when we start
        self._loadedObjects = []

    def load(self) -> None:
        """ Load

        This will be called when the plugin is loaded, just after the db is migrated.
        Place any custom initialiastion steps here.

        """
        logger.debug("Loaded")

    def start(self):
        """ Load

        This will be called when the plugin is loaded, just after the db is migrated.
        Place any custom initialiastion steps here.

        """
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
    def celeryAppIncludes(self):
        return [RandomNumber.__name__]
