from vortex.handler.TupleDataObservableHandler import logger
from vortex.sqla_orm.OrmCrudHandler import OrmCrudHandler

from peek_plugin_tutorial._private.PluginNames import tutorialFilt
from peek_plugin_tutorial._private.storage.Setting import SettingProperty, globalSetting

# This dict matches the definition in the Admin angular app.
filtKey = {"key": "admin.Edit.SettingProperty"}
filtKey.update(tutorialFilt)


# This is the CRUD handler
class __CrudHandler(OrmCrudHandler):
    # The UI only edits the global settings
    # You could get more complicated and have the UI edit different groups of settings.
    def createDeclarative(self, session, payloadFilt):
        return [p for p in globalSetting(session).propertyObjects]


# This method creates an instance of the handler class.
def makeSettingPropertyHandler(dbSessionCreator):
    handler = __CrudHandler(dbSessionCreator, SettingProperty,
                            filtKey, retreiveAll=True)

    logger.debug("Started")
    return handler