import {CommonModule} from "@angular/common";
import {NgModule} from "@angular/core";
import {Routes} from "@angular/router";

// Import a small abstraction library to switch between NativeScript and web
import {PeekModuleFactory} from "@synerty/peek-web-ns/index.web";

// Import the default route component
import {TutorialComponent} from "./tutorial.component";

// Import the required classes from VortexJS
import {TupleOfflineStorageNameService, TupleOfflineStorageService} from "@synerty/vortexjs";

// Import the names we need for the
import {tutorialTupleOfflineServiceName} from "@peek/peek_plugin_tutorial/_private";

// Import the required classes from VortexJS
import {TupleDataObservableNameService, TupleDataObserverService, TupleDataOfflineObserverService} from "@synerty/vortexjs";

// Import the names we need for the
import {tutorialObservableName, tutorialFilt} from "@peek/peek_plugin_tutorial/_private";


export function tupleDataObservableNameServiceFactory() {
    return new TupleDataObservableNameService(
        tutorialObservableName, tutorialFilt);
}

export function tupleOfflineStorageNameServiceFactory() {
    return new TupleOfflineStorageNameService(tutorialTupleOfflineServiceName);
}

// Define the child routes for this plugin
export const pluginRoutes: Routes = [
    {
        path: '',
        component: TutorialComponent
    },
    {
        path: '**',
        component: TutorialComponent
    }

];

// Define the root module for this plugin.
// This module is loaded by the lazy loader, what ever this defines is what is started.
// When it first loads, it will look up the routs and then select the component to load.
@NgModule({
    imports: [
        CommonModule,
        PeekModuleFactory.RouterModule.forChild(pluginRoutes)],
    exports: [],
    providers: [
        TupleOfflineStorageService, {
        provide: TupleOfflineStorageNameService,
        useFactory:tupleOfflineStorageNameServiceFactory
        },
        TupleDataObserverService, TupleDataOfflineObserverService, {
        provide: TupleDataObservableNameService,
        useFactory: tupleDataObservableNameServiceFactory
        },
    ],
    declarations: [TutorialComponent]
})
export class TutorialModule
{
}
