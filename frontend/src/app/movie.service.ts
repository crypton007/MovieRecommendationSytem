import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Movies } from './movies';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  private baseURL = "http://localhost:8081/api/movies"

  constructor(private httpClient: HttpClient) { }

  getMovieList(): Observable<Movies[]>{
     return this.httpClient.get<Movies[]>('http://127.0.0.1:5000/allmovies');
  }

  searchByTitle(title:string): Observable<Movies[]>{
      return this.httpClient.get<Movies[]>('http://127.0.0.1:5000/titlesearch?title='+title);
 }

}
