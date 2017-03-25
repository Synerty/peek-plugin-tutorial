                                         import {addTupleType, Tuple, TupleActionABC} from "@synerty/vortexjs";
import {tutorialTuplePrefix} from "../PluginNames";

@addTupleType
export class StringIntDecreaseActionTuple extends TupleActionABC {
    static readonly tupleName = tutorialTuplePrefix + "StringIntDecreaseActionTuple";

    stringIntId: number;
    offset: number;

    constructor() {
        super(StringIntDecreaseActionTuple.tupleName)
    }
}