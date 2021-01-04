import logging
from twisted.internet import task, reactor, defer
from twisted.internet.defer import inlineCallbacks
from vortex.DeferUtil import deferToThreadWrapWithLogger, vortexLogFailure
from datetime import datetime
from random import randint
import pytz

logger = logging.getLogger(__name__)


class RandomNumberWorkerController:
    """Random Number Generator

    Generates random number on worker periodically
    """

    PERIOD = 5
    TASK_TIMEOUT = 60.0

    def __init__(self):
        self._pollLoopingCall = task.LoopingCall(self._poll)

    def start(self):
        d = self._pollLoopingCall.start(self.PERIOD, now=False)
        d.addCallbacks(self._timerCallback, self._timerErrback)

    def _timerErrback(self, failure):
        vortexLogFailure(failure, logger)

    def _timerCallback(self, _):
        logger.info("Time executed successfully")

    def stop(self):
        if self._pollLoopingCall.running:
            self._pollLoopingCall.stop()

    def shutdown(self):
        self.stop()

    @inlineCallbacks
    def _poll(self):
        # Send the tasks to the peek worker
        start = randint(1, 1000)
        try:
            result = yield self._sendToWorker(start)
        except Exception as e:
            logger.exception(e)

    @inlineCallbacks
    def _sendToWorker(self, item):
        from peek_plugin_tutorial._private.worker.tasks.RandomNumber import (
            pickRandomNumber,
        )

        startTime = datetime.now(pytz.utc)

        try:
            d = pickRandomNumber.delay(item)
            d.addTimeout(self.TASK_TIMEOUT, reactor)
            randomNumber = yield d
            logger.debug(
                "Time Taken = %s, Random Number: %s"
                % (datetime.now(pytz.utc) - startTime, randomNumber)
            )
        except Exception as e:
            logger.debug(" RandomNumber task failed : %s", str(e))
