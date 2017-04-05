from .SettingPropertyHandler import makeSettingPropertyHandler


def makeAdminBackendHandlers(dbSessionCreator):
    yield makeSettingPropertyHandler(dbSessionCreator)
    pass
