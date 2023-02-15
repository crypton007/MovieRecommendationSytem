import { Component } from '@angular/core';
import { Top10movies } from '../top10movies';
import { InputTextModule } from 'primeng/inputtext';
import { ButtonModule } from 'primeng/button';
import { Top10moviesService } from '../top10movies.service';

@Component({
  selector: 'app-top10movies',
  templateUrl: './top10movies.component.html',
  styleUrls: ['./top10movies.component.css'],
})

export class Top10moviesComponent {

  top10movies: Top10movies[];
  // genre:string;

  private getTopMovies(){
    this.top10moviesService.getTopMovieList().subscribe(data => {
      this.top10movies = data;
    });
    console.log(this.top10movies);
  }
  ngOnInit(): void{


    this.getTopMovies();
  }

  constructor(private top10moviesService: Top10moviesService){}

  genres = ['Action','Adventure','Animation','Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','IMAX','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','(no genres listed)'];
  selectedGenres = [];

  search(selectedGenres: string[]) {
    const genreString = selectedGenres.join(',');
    this.top10moviesService.getGenre(genreString).subscribe((data) => {
      this.top10movies = data;
    }, (error) => {
      console.log(error);
    });
  }


}
