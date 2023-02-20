import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MovieListComponent } from './movie-list/movie-list.component';
import { Similaruser } from './similaruser';
import { SimilaruserComponent } from './similaruser/similaruser.component';
import { Top10moviesComponent } from './top10movies/top10movies.component';
import { UserrecoomendationComponent } from './userrecoomendation/userrecoomendation.component';

const routes: Routes = [
  {path:'movie-list', component:MovieListComponent},
  {path:'top10movies',component:Top10moviesComponent},
  {path:'userrecommendations',component:UserrecoomendationComponent},
  {path:'Similarusers',component:SimilaruserComponent},
  {path:'',redirectTo:'movie-list',pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
