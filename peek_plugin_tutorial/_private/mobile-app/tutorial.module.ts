import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { Routes } from "@angular/router";
import { HttpClientModule } from "@angular/common/http";
import { FormsModule } from "@angular/forms";
import { NzIconModule } from "ng-zorro-antd/icon";
import { RouterModule } from "@angular/router";
import {
    TupleOfflineStorageNameService,
    TupleOfflineStorageService,
    TupleDataObservableNameService,
    TupleDataObserverService,
    TupleDataOfflineObserverService,
    TupleActionPushNameService,
    TupleActionPushOfflineService,
    TupleActionPushService,
} from "@synerty/vortexjs";
import {
    tutorialTupleOfflineServiceName,
    tutorialObservableName,
    tutorialFilt,
    tutorialActionProcessorName,
} from "@_peek/peek_plugin_tutorial/_private";
import { TutorialComponent } from "./tutorial.component";
import { StringIntComponent } from "./string-int/string-int.component";

export function tupleOfflineStorageNameServiceFactory() {
    return new TupleOfflineStorageNameService(tutorialTupleOfflineServiceName);
}

export function tupleDataObservableNameServiceFactory() {
    return new TupleDataObservableNameService(
        tutorialObservableName,
        tutorialFilt
    );
}

export function tupleActionPushNameServiceFactory() {
    return new TupleActionPushNameService(
        tutorialActionProcessorName,
        tutorialFilt
    );
}

export const pluginRoutes: Routes = [
    {
        path: "stringint",
        component: StringIntComponent,
    },
    {
        path: "",
        pathMatch: "full",
        component: TutorialComponent,
    },
];

@NgModule({
    imports: [
        CommonModule,
        HttpClientModule,
        RouterModule.forChild(pluginRoutes),
        FormsModule,
        NzIconModule,
    ],
    exports: [],
    providers: [
        TupleOfflineStorageService,
        {
            provide: TupleOfflineStorageNameService,
            useFactory: tupleOfflineStorageNameServiceFactory,
        },
        TupleDataObserverService,
        TupleDataOfflineObserverService,
        {
            provide: TupleDataObservableNameService,
            useFactory: tupleDataObservableNameServiceFactory,
        },
        TupleActionPushOfflineService,
        TupleActionPushService,
        {
            provide: TupleActionPushNameService,
            useFactory: tupleActionPushNameServiceFactory,
        },
    ],
    declarations: [TutorialComponent, StringIntComponent],
})
export class TutorialModule {}
