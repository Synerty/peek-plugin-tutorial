import { addTupleType, TupleActionABC } from "@synerty/vortexjs";
import { tutorialTuplePrefix } from "../PluginNames";

@addTupleType
export class AddIntValueActionTuple extends TupleActionABC {
    public static readonly tupleName =
        tutorialTuplePrefix + "AddIntValueActionTuple";

    stringIntId: number;
    offset: number;

    constructor() {
        super(AddIntValueActionTuple.tupleName);
    }
}
