import logging

from peek_plugin_base.server.PluginServerEntryHookABC import PluginServerEntryHookABC

from peek_plugin_tutorial._private.storage import DeclarativeBase
from peek_plugin_tutorial._private.storage.DeclarativeBase import loadStorageTuples
from peek_plugin_base.server.PluginServerStorageEntryHookABC import PluginServerStorageEntryHookABC


from peek_plugin_tutorial._private.tuples import loadPrivateTuples
from peek_plugin_tutorial.tuples import loadPublicTuples


from .admin_backend import makeAdminBackendHandlers

from .TupleDataObservable import makeTupleDataObservableHandler
from .TupleActionProcessor import makeTupleActionProcessorHandler
from .controller.MainController import MainController



from .agent_handlers.RpcForAgent import RpcForAgent
from .ServerToAgentRpcCallExample import ServerToAgentRpcCallExample


from .TutorialApi import TutorialApi
from peek_plugin_inbox.server.InboxApiABC import InboxApiABC
from .ExampleUseTaskApi import ExampleUseTaskApi


from peek_plugin_base.server.PluginServerWorkerEntryHookABC import PluginServerWorkerEntryHookABC
from peek_plugin_tutorial._private.server.controller.RandomNumberWorkerController import RandomNumberWorkerController

logger = logging.getLogger(__name__)

class ServerEntryHook(PluginServerEntryHookABC, PluginServerStorageEntryHookABC, PluginServerWorkerEntryHookABC):
    def __init__(self, *args, **kwargs):
        """" Constructor """
        # Call the base classes constructor
        PluginServerEntryHookABC.__init__(self, *args, **kwargs)

        #: Loaded Objects, This is a list of all objects created when we start
        self._loadedObjects = []
        
        self._api = None
        

    def load(self) -> None:
        """ Load

        This will be called when the plugin is loaded, just after the db is migrated.
        Place any custom initialiastion steps here.

        """
        
        loadStorageTuples() # <-- Add this line
        
        
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
        mainController = MainController(dbSessionCreator=self.dbSessionCreator, tupleObservable=tupleObservable)

        self._loadedObjects.append(mainController)
        self._loadedObjects.append(makeTupleActionProcessorHandler(mainController))
        
        
        
        # Initialise the RpcForAgent
        self._loadedObjects.extend(RpcForAgent(mainController, self.dbSessionCreator)
                           .makeHandlers())
        # Initialise and start the RPC for Server
        self._loadedObjects.append(ServerToAgentRpcCallExample().start())
        
        
        # Initialise the API object that will be shared with other plugins
        self._api = TutorialApi(mainController)
        self._loadedObjects.append(self._api)
        # Get a reference for the Active Task
        inboxApi = self.platform.getOtherPluginApi("peek_plugin_inbox")
        assert isinstance(inboxApi, InboxApiABC), "Wrong inboxApi"
        # Initialise the example code that will send the test task
        self._loadedObjects.append(ExampleUseTaskApi(mainController, inboxApi).start())
        
        
        randomNumberController = RandomNumberWorkerController()
        self._loadedObjects.append(randomNumberController)
        randomNumberController.start()
        
        logger.debug("Started")

    def stop(self):
        """ Stop

        This method is called by the platform to tell the peek app to shutdown and stop
        everything it's doing
        """
        # Shutdown and dereference all objects we constructed when we started
        while self._loadedObjects:
            self._loadedObjects.pop().shutdown()
        
        self._api = None
        
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
    

    
    @property
    def publishedServerApi(self) -> object:
        """ Published Server API

        :return  class that implements the API that can be used by other Plugins on this
        platform service.
        """
        return self._api
    
