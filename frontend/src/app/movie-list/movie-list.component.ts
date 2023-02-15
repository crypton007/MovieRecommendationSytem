import { Component } from '@angular/core';
// import DataTables from 'datatables.net-dt';
// import DataTables from 'datatables.net';
// import DataTables from 'datatables.net';
import { MovieService } from '../movie.service';
import { Movies } from '../movies';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent {

  movies: Movies[];

  dtOptions: DataTables.Settings = {};

  constructor(private movieService: MovieService){}

  private getMovies(){
    this.movieService.getMovieList().subscribe(data => {
      this.movies = data;
    });
  }

  ngOnInit(): void{

    this.dtOptions = {
      pagingType: 'full_numbers',
      pageLength: 10,
      processing: true
    };

    this.getMovies();
  }

  searchByTitle(title: HTMLInputElement) {
    this.movieService.searchByTitle(title.value).subscribe((data) => {
      this.movies = data;
    }, (error) => {
      console.log(error);
    });
  }
 
}
