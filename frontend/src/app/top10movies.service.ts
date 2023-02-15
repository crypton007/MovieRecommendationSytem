import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Top10movies } from './top10movies';

@Injectable({
  providedIn: 'root'
})
export class Top10moviesService {

  private baseURL = "http://localhost:8081/api/movies"

  constructor(private httpClient: HttpClient) { }

  getGenre(genre:string): Observable<Top10movies[]>{
    console.log(genre)
    return this.httpClient.get<Top10movies[]>('http://127.0.0.1:5000/topmovies?genre='+genre);
 }

 getTopMovieList(): Observable<Top10movies[]>{
  return this.httpClient.get<Top10movies[]>('http://127.0.0.1:5000/topmovies');
}


}
