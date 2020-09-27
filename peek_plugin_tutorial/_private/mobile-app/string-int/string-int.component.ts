import { Component } from "@angular/core"
import { Router } from "@angular/router"
import {
    AddIntValueActionTuple,
    StringCapToggleActionTuple,
    StringIntTuple,
    tutorialBaseUrl,
} from "@_peek/peek_plugin_tutorial/_private"
import { TupleActionPushService, TupleDataObserverService, TupleSelector } from "@synerty/vortexjs"
import { NgLifeCycleEvents } from "@synerty/peek-plugin-base-js"

@Component({
    selector: "plugin-tutorial-string-int",
    templateUrl: "string-int.component.mweb.html",
    moduleId: module.id
})
export class StringIntComponent extends NgLifeCycleEvents {
    stringInts: Array<StringIntTuple> = []
    
    constructor(
        private tupleDataObserver: TupleDataObserverService,
        // private tupleDataObserver: TupleDataOfflineObserverService,
        private router: Router,
        private actionService: TupleActionPushService,
    ) {
        super()
        
        // Create the TupleSelector to tell the obserbable what data we want
        let selector = {}
        // Add any filters of the data here
        // selector["lookupName"] = "brownCowList";
        let tupleSelector = new TupleSelector(StringIntTuple.tupleName, selector)
        
        // Setup a subscription for the data
        let sup = tupleDataObserver.subscribeToTupleSelector(tupleSelector)
            .subscribe((tuples: StringIntTuple[]) => {
                // We've got new data, assign it to our class variable
                this.stringInts = tuples
            })
        
        // unsubscribe when this component is destroyed
        // This is a feature of NgLifeCycleEvents
        this.onDestroyEvent.subscribe(() => sup.unsubscribe())
    }
    
    mainClicked() {
        this.router.navigate([tutorialBaseUrl])
    }
    
    toggleUpperClicked(item) {
        let action = new StringCapToggleActionTuple()
        action.stringIntId = item.id
        this.actionService.pushAction(action)
            .then(() => {
                alert("success")
                
            })
            .catch((err) => {
                alert(err)
            })
    }
    
    incrementClicked(item) {
        let action = new AddIntValueActionTuple()
        action.stringIntId = item.id
        action.offset = 1
        this.actionService.pushAction(action)
            .then(() => {
                alert("success")
                
            })
            .catch((err) => {
                alert(err)
            })
    }
    
    decrementClicked(item) {
        let action = new AddIntValueActionTuple()
        action.stringIntId = item.id
        action.offset = -1
        this.actionService.pushAction(action)
            .then(() => {
                alert("success")
            })
            .catch((err) => {
                alert(err)
            })
    }
}
