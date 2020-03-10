import { Component, OnInit, Input } from '@angular/core';
import { RestService } from '../rest.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormControl, FormsModule } from '@angular/forms';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-user-add',
  templateUrl: './user-add.component.html',
  styleUrls: ['./user-add.component.css'],
})
export class UserAddComponent implements OnInit { 

  @Input() userData = { name:'',dateOfBirth: '' , email: ''  ,contact: ''};
  temp={dateS:''};

  constructor(public rest:RestService, private route: ActivatedRoute, private router: Router ) { }
  
  dateMin;
  today=new Date();
  lol=this.temp.dateS;
  // lol=this.today;

  ngOnInit() {
    this.dateMin=new Date(this.today.getFullYear() - 18, this.today.getMonth(), this.today.getDate());
  }
  
  addUser() {
    this.userData.dateOfBirth=this.temp.dateS.toString()
    this.rest.addUser(this.userData).subscribe((result) => {
      this.router.navigate(['/user-details/'+result._id]);
    }, (err) => {
      console.log(err);
    });
  }
}
      
interface Validator<T extends FormControl> {
  (c:T): {[error: string]:any};
}