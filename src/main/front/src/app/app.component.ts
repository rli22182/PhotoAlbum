import {Component, OnInit} from '@angular/core';
import {UserService} from './user.service';
import {User} from './user';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css'],
    template: `
  <div style="width: 100%; overflow: hidden;">
<div style="width: 400px; float: left;">
<ul class="users">
<li *ngFor="let user of users"
[class.selected]="user === selectedUser"
(click)="onSelect(user)">

    <!-- each user goes here -->
    <span class="badge">{{user.id}}</span> {{user.name}}
  </li>
</ul>
</div>
<div style="margin-left: 420px;" *ngIf="selectedUser">
  <h2>{{selectedUser.name}}</h2>
  <div><label>id: </label>{{selectedUser.id}}</div>
  <div>
    <label>name: </label>
    <input [(ngModel)]="selectedUser.name" placeholder="name"/>
  </div>
  <div>
    <label>username: </label>
    <input [(ngModel)]="selectedUser.username" placeholder="username"/>
  </div>
  <div>
    <label>email: </label>
    <input [(ngModel)]="selectedUser.email" placeholder="email"/>
  </div>
  <div>
  <h3>Address</h3>
  <div>
    <label>street: </label>
    <label> {{selectedUser.address.street}} </label>
  </div>
  <div>
    <label>suite: </label>
    <label> {{selectedUser.address.suite}} </label>
  </div>
  <div>
    <label>city: </label>
    <label> {{selectedUser.address.city}} </label>
  </div>
  <div>
    <label>zipcode: </label>
    <label> {{selectedUser.address.zipcode}} </label>
  </div>
  </div>
</div>
</div>
  `,
    providers: [UserService]

})
export class AppComponent implements OnInit {
    title = 'Photo Album';
    selectedUser: User;
    errorMessage: string;
    users: User[];

    constructor(private userService: UserService) {
    }

    onSelect(user: User) {
        this.selectedUser = user;
    }

    ngOnInit() {
        this.getUsers();
    }

    getUsers() {
        this.userService.getUsers()
            .then(
                users => this.users = users,
                error => this.errorMessage = <any>error);
    }

}
