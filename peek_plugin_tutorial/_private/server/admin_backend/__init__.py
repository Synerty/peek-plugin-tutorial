from .StringIntTableHandler import makeStringIntTableHandler
from .SettingPropertyHandler import makeSettingPropertyHandler

def makeAdminBackendHandlers(dbSessionCreator):
    yield makeStringIntTableHandler(dbSessionCreator)
    yield makeSettingPropertyHandler(dbSessionCreator)
