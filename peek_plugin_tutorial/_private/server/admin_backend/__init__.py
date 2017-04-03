from .StringIntTableHandler import makeStringIntTableHandler

from .SettingPropertyHandler import makeSettingPropertyHandler


def makeAdminBackendHandlers(dbSessionCreator):
    yield makeSettingPropertyHandler(tupleObservable, dbSessionCreator)
    pass
