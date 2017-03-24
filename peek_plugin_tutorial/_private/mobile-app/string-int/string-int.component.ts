import {Component} from "@angular/core";
import {Router} from "@angular/router";
import {StringIntTuple, tutorialBaseUrl} from "@peek/peek_plugin_tutorial/_private";

import {
    ComponentLifecycleEventEmitter,
    TupleDataObserverService,
    TupleSelector
} from "@synerty/vortexjs";

@Component({
    selector: 'plugin-tutorial-string-int',
    templateUrl: 'string-int.component.mweb.html',
    moduleId: module.id
})
export class StringIntComponent extends ComponentLifecycleEventEmitter {

    stringInts: Array<StringIntTuple> = [];

    constructor(private tupleDataObserver: TupleDataObserverService,
                private router: Router) {
        super();

        // Create the TupleSelector to tell the obserbable what data we want
        let selector = {};
        // Add any filters of the data here
        // selector["lookupName"] = "brownCowList";
        let tupleSelector = new TupleSelector(StringIntTuple.tupleName, selector);

        // Setup a subscription for the data
        let sup = tupleDataObserver.subscribeToTupleSelector(tupleSelector)
            .subscribe((tuples: StringIntTuple[]) => {
                // We've got new data, assign it to our class variable
                this.stringInts = tuples;
            });

        // unsubscribe when this component is destroyed
        // This is a feature of ComponentLifecycleEventEmitter
        this.onDestroyEvent.subscribe(() => sup.unsubscribe());

    }

    mainClicked() {
        this.router.navigate([tutorialBaseUrl]);
    }

}