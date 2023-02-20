import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Similaruser } from './similaruser';

@Injectable({
  providedIn: 'root'
})
export class SimilaruserService {


  constructor(private httpClient: HttpClient) { }

  searchByUserid(userid:string): Observable<Similaruser[]>{
      console.log('http://127.0.0.1:5000/v?userid='+userid)
      return this.httpClient.get<Similaruser[]>('http://127.0.0.1:5000/similaruserids?userid='+userid);
 }

}
