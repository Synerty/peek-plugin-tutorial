from .StringIntTableHandler import makeStringIntTableHandler

def makeAdminBackendHandlers(dbSessionCreator):
    yield makeStringIntTableHandler(dbSessionCreator)