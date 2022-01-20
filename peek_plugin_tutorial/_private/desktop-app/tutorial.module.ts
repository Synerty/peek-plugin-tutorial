import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { FormsModule } from "@angular/forms";
import { NzIconModule } from "ng-zorro-antd/icon";
import { HttpClientModule } from "@angular/common/http";
import { TutorialComponent } from "./tutorial.component";

export const pluginRoutes: Routes = [
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
    providers: [],
    declarations: [TutorialComponent],
})
export class TutorialModule {}
