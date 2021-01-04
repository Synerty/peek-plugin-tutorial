import { Component } from "@angular/core"
import {
    BalloonMsgService,
    NgLifeCycleEvents
} from "@synerty/peek-plugin-base-js"
import { extend, TupleLoader, VortexService } from "@synerty/vortexjs"
import {
    StringIntTuple,
    tutorialFilt
} from "@peek/peek_plugin_tutorial/_private"

@Component({
    selector: "pl-tutorial-edit-string-int",
    templateUrl: "./edit.component.html"
})
export class EditStringIntComponent extends NgLifeCycleEvents {
    items: StringIntTuple[] = []
    itemsToDelete: StringIntTuple[] = []
    loader: TupleLoader
    // This must match the dict defined in the admin_backend handler
    private readonly filt = {
        "key": "admin.Edit.StringIntTuple"
    }
    
    constructor(
        private balloonMsg: BalloonMsgService,
        vortexService: VortexService
    ) {
        super()
        
        this.loader = vortexService.createTupleLoader(this,
            () => {
                let filt = extend({}, this.filt, tutorialFilt)
                // If we wanted to filter the data we get, we could add this
                // filt["lookupName"] = 'lookupType';
                return filt
            })
        
        this.loader.observable
            .subscribe((tuples: StringIntTuple[]) => {
                this.items = tuples
                this.itemsToDelete = []
            })
    }
    
    addRow() {
        let t = new StringIntTuple()
        // Add any values needed for this list here, EG, for a lookup list you might add:
        // t.lookupName = this.lookupName;
        this.items.push(t)
    }
    
    removeRow(item) {
        if (item.id != null)
            this.itemsToDelete.push(item)
        
        let index: number = this.items.indexOf(item)
        if (index !== -1) {
            this.items.splice(index, 1)
        }
    }
    
    save() {
        let itemsToDelete = this.itemsToDelete
        
        this.loader.save(this.items)
            .then(() => {
                if (itemsToDelete.length != 0) {
                    return this.loader.del(itemsToDelete)
                }
            })
            .then(() => this.balloonMsg.showSuccess("Save Successful"))
            .catch(e => this.balloonMsg.showError(e))
    }
    
    resetClicked() {
        this.loader.load()
            .then(() => this.balloonMsg.showSuccess("Reset Successful"))
            .catch(e => this.balloonMsg.showError(e))
    }
}
