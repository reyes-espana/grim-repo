import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WeekComponent } from './week/week.component';

const routes: Routes = [
  { path: '', redirectTo: '/week', pathMatch: 'full' },
  { path: 'week', component: WeekComponent }, 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
