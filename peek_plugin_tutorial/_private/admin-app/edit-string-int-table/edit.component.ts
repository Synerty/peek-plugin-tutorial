import {Component, OnInit} from "@angular/core";
import {
    extend,
    VortexService,
    ComponentLifecycleEventEmitter,
    TupleLoader
} from "@synerty/vortexjs";
import {StringIntTuple,
    tutorialPluginFilt
} from "@peek/peek_plugin_tutorial/_private";


@Component({
    selector: 'pl-tutorial-edit-string-int',
    templateUrl: './edit.component.html'
})
export class EditStringIntComponent extends ComponentLifecycleEventEmitter {
    // This must match the dict defined in the admin_backend handler
    private readonly filt = {
        "key": "admin.Edit.StringIntTuple"
    };

    items: StringIntTuple[] = [];

    loader: TupleLoader;

    constructor(vortexService: VortexService) {
        super();

        this.loader = vortexService.createTupleLoader(this,
            () => extend({}, this.filt, tutorialPluginFilt));

        this.loader.observable
            .subscribe((tuples:StringIntTuple[]) => this.items = tuples);
    }

    addRow() {
        this.items.push(new StringIntTuple());
    }

    removeRow(item) {
        if (confirm("Delete Row? All unsaved changes will be lost.")) {
            this.loader.del([item]);
        }
    }

}