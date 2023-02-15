import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MovieListComponent } from './movie-list/movie-list.component';
import { Top10moviesComponent } from './top10movies/top10movies.component';

const routes: Routes = [
  {path:'movie-list', component:MovieListComponent},
  {path:'top10movies',component:Top10moviesComponent},
  {path:'',redirectTo:'movie-list',pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
