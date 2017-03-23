from .StringIntTableHandler import makeStringIntTableHandler

from vortex.handler.TupleDataObservableHandler import TupleDataObservableHandler


def makeAdminBackendHandlers(tupleObservable: TupleDataObservableHandler,
                             dbSessionCreator):
    yield makeStringIntTableHandler(tupleObservable, dbSessionCreator)
