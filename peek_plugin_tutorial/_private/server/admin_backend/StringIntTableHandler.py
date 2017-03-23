from peek_plugin_tutorial._private.PluginNames import tutorialFilt
from peek_plugin_tutorial._private.storage.StringIntTuple import StringIntTuple
from vortex.handler.TupleDataObservableHandler import logger
from vortex.sqla_orm.OrmCrudHandler import OrmCrudHandler

# This dict matches the definition in the Admin angular app.
filtKey = {"key": "admin.Edit.StringIntTuple"}
filtKey.update(tutorialFilt)


# This is the CRUD hander
class __CrudHandler(OrmCrudHandler):
    pass


# This method creates an instance of the handler class.
def makeStringIntTableHandler(dbSessionCreator):
    handler = __CrudHandler(dbSessionCreator, StringIntTuple,
                            filtKey, retreiveAll=True)

    logger.debug("Started")
    return handler
