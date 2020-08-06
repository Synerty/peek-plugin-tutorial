import {CommonModule} from "@angular/common";
import {NgModule} from "@angular/core";
import {Routes} from "@angular/router";

// Import a small abstraction library to switch between nativescript and web
import {PeekModuleFactory} from "@synerty/peek-util-web";

// Import the default route component
import {TutorialComponent} from "./tutorial.component";


// Define the child routes for this plugin
export const pluginRoutes: Routes = [
    {
        path: '',
        pathMatch:'full',
        component: TutorialComponent
    }

];

// Define the root module for this plugin.
// This module is loaded by the lazy loader, what ever this defines is what is started.
// When it first loads, it will look up the routs and then select the component to load.
@NgModule({
    imports: [
        CommonModule,
        PeekModuleFactory.RouterModule,
        PeekModuleFactory.RouterModule.forChild(pluginRoutes),
        ...PeekModuleFactory.FormsModules
    ],
    exports: [],
    providers: [],
    declarations: [TutorialComponent]
})
export class TutorialModule
{
}
