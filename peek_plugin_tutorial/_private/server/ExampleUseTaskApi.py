import logging
import pytz
from datetime import datetime

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from peek_plugin_inbox.server.InboxApiABC import InboxApiABC, NewTask
from peek_plugin_tutorial._private.server.controller.MainController import (
    MainController,
)
from peek_plugin_tutorial._private.PluginNames import tutorialPluginName

logger = logging.getLogger(__name__)


class ExampleUseTaskApi:
    def __init__(self, mainController: MainController, inboxApi: InboxApiABC):
        self._mainController = mainController
        self._inboxApi = inboxApi

    def start(self):
        reactor.callLater(1, self.sendTask)
        return self

    @inlineCallbacks
    def sendTask(self):
        # First, create the task
        newTask = NewTask(
            pluginName=tutorialPluginName,
            uniqueId=str(datetime.now(pytz.utc)),
            userId="1",  # <----- Set to your user id
            title="A task from tutorial plugin",
            description="Tutorials task description",
            routePath="/peek_plugin_tutorial",
            autoDelete=NewTask.AUTO_DELETE_ON_SELECT,
            overwriteExisting=True,
            notificationRequiredFlags=NewTask.NOTIFY_BY_DEVICE_SOUND
            | NewTask.NOTIFY_BY_EMAIL,
        )

        # Now send the task via the active tasks API
        yield self._inboxApi.addTask(newTask)
        logger.debug("Task Sent")

    def shutdown(self):
        pass
