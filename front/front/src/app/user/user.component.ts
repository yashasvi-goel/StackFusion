import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  user:any = [];

  constructor(public rest:RestService, private route: ActivatedRoute, private router: Router) { }

  ngOnInit() {
    this.getAllData();
  }

  getAllData() {
    this.user = [];
    this.rest.getAllData().subscribe((data: {}) => {
      console.log(data);
      this.user = data;
    });
  }

  add() {
    this.router.navigate(['/user-add']);
  }

  // delete(id) {
  //   this.rest.deleteUser(id)
  //     .subscribe(res => {
  //         this.getAllData();
  //       }, (err) => {
  //         console.log(err);
  //       }
  //     );
  // }

}