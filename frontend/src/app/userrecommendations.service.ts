import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Movies } from './movies';
import {userrecommendations} from './userrecommendations'

@Injectable({
  providedIn: 'root'
})
export class UserrecommendationsService {

  private baseURL = "http://localhost:8081/api/movies"

  constructor(private httpClient: HttpClient) { }

  searchByUserid(userid:string): Observable<userrecommendations[]>{
      console.log('http://127.0.0.1:5000/recommendations?userid='+userid)
      return this.httpClient.get<userrecommendations[]>('http://127.0.0.1:5000/recommendations?userid='+userid);
 }

}
