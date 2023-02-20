import { Component } from '@angular/core';
import { Similaruser } from '../similaruser';
import { SimilaruserService } from '../similaruser.service';

@Component({
  selector: 'app-similaruser',
  templateUrl: './similaruser.component.html',
  styleUrls: ['./similaruser.component.css']
})
export class SimilaruserComponent {

  users: Similaruser[];

  dtOptions: DataTables.Settings = {};

  constructor(private SimilaruserService: SimilaruserService){}

  ngOnInit(): void{

    // this.dtOptions = {
    //   pagingType: 'full_numbers',
    //   pageLength: 10,
    //   processing: true
    // };

    // this.getMovies();
  }

  searchByUserid(userid: HTMLInputElement) {
    this.SimilaruserService.searchByUserid(userid.value).subscribe((data) => {
      this.users = data;
      console.log(data)
    }, (error) => {
      console.log(error);
    });
  }

}
