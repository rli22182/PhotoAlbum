import {Component, OnInit} from '@angular/core';
import {UserService} from './user.service';
import {User} from './user';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css'],
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
