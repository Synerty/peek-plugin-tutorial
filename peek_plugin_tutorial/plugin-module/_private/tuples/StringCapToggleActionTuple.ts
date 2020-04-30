import {addTupleType, Tuple, TupleActionABC} from "@synerty/vortexjs";
import {tutorialTuplePrefix} from "../PluginNames";

@addTupleType
export class StringCapToggleActionTuple extends TupleActionABC {
    public static readonly tupleName = tutorialTuplePrefix + "StringCapToggleActionTuple";

    stringIntId: number;

    constructor() {
        super(StringCapToggleActionTuple.tupleName)
    }
}
