from vortex.Tuple import addTupleType, TupleField
from vortex.TupleAction import TupleActionABC

from peek_plugin_tutorial._private.PluginNames import tutorialTuplePrefix


@addTupleType
class StringIntDecreaseActionTuple(TupleActionABC):
    __tupleType__ = tutorialTuplePrefix + "StringIntDecreaseActionTuple"

    stringIntId = TupleField()
    offset = TupleField()
