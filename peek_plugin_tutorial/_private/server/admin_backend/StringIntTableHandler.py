import logging

from peek_plugin_tutorial._private.PluginNames import tutorialFilt
from peek_plugin_tutorial._private.storage.StringIntTuple import StringIntTuple

from vortex.sqla_orm.OrmCrudHandler import OrmCrudHandler

logger = logging.getLogger(__name__)

# This dict matches the definition in the Admin angular app.
filtKey = {"key": "admin.Edit.StringIntTuple"}
filtKey.update(tutorialFilt)


# This is the CRUD hander
class __CrudHandler(OrmCrudHandler):
    pass

    # If we only wanted to edit a subset of the data, this is how it's done
    # def createDeclarative(self, session, payloadFilt):
    #     lookupName = payloadFilt["lookupName"]
    #     return (session.query(StringIntTuple)
    #             .filter(StringIntTuple.lookupName == lookupName)
    #             .all())


# This method creates an instance of the handler class.
def makeStringIntTableHandler(dbSessionCreator):
    handler = __CrudHandler(dbSessionCreator, StringIntTuple,
                            filtKey, retreiveAll=True)

    logger.debug("Started")
    return handler
