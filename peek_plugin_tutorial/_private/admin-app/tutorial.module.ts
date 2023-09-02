import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { NgModule } from "@angular/core";
import { RouterModule, Route, Routes } from "@angular/router";

// Import our components
import { TutorialComponent } from "./tutorial.component";
import { EditStringIntComponent } from "./edit-string-int-table/edit.component";
import { EditSettingComponent } from "./edit-setting-table/edit.component";

// Define the routes for this Angular module
export const pluginRoutes: Routes = [
    {
        path: "",
        pathMatch: "full",
        component: TutorialComponent,
    },
];

// Define the module
@NgModule({
    imports: [CommonModule, RouterModule.forChild(pluginRoutes), FormsModule],
    exports: [],
    providers: [],
    declarations: [
        TutorialComponent,
        EditStringIntComponent,
        EditSettingComponent,
    ],
})
export class TutorialModule {}
