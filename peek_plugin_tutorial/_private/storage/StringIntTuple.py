from sqlalchemy import Column
from sqlalchemy import Integer, String
from vortex.Tuple import Tuple, addTupleType

from peek_plugin_tutorial._private.PluginNames import tutorialTuplePrefix
from peek_plugin_tutorial._private.storage.DeclarativeBase import DeclarativeBase


@addTupleType
class StringIntTuple(DeclarativeBase, Tuple):
    __tupleType__ = tutorialTuplePrefix + "StringIntTuple"
    __tablename__ = "StringIntTuple"

    id = Column(Integer, primary_key=True, autoincrement=True)
    string1 = Column(String)
    int1 = Column(Integer)
