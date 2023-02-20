import { Component } from '@angular/core';
import { userrecommendations } from '../userrecommendations';
import { UserrecommendationsService } from '../userrecommendations.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-userrecoomendation',
  templateUrl: './userrecoomendation.component.html',
  styleUrls: ['./userrecoomendation.component.css']
})
export class UserrecoomendationComponent {

  recommendations: userrecommendations[];

  dtOptions: DataTables.Settings = {};

  constructor(private UserrecommendationsService: UserrecommendationsService){}

  ngOnInit(): void{

    // this.dtOptions = {
    //   pagingType: 'full_numbers',
    //   pageLength: 10,
    //   processing: true
    // };

    // this.getMovies();
  }

  searchByUserid(userid: HTMLInputElement) {
    this.UserrecommendationsService.searchByUserid(userid.value).subscribe((data) => {
      this.recommendations = data;
      console.log(data)
    }, (error) => {
      console.log(error);
    });
  }

  
}
