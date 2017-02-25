import {Component, OnInit} from '@angular/core';
import {UserService} from './user.service';
import {User} from './user';

@Component({
    selector: 'users',
    templateUrl: './users.component.html',
    styleUrls: ['./users.component.css'],
    providers: [UserService]

})
export class UsersComponent implements OnInit {
    title = 'Users';
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
