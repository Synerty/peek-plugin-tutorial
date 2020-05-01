import logging
from random import randint
from txcelery.defer import DeferrableTask
from peek_plugin_base.worker.CeleryApp import celeryApp

logger = logging.getLogger(__name__)


@DeferrableTask
@celeryApp.task(bind=True)
def pickRandomNumber(self, item: int) -> int:
    """
    Returns random integer between 1 to 1000
    """
    logger.debug("Received item:".format(item))
    return int(item) * -1
