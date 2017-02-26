// Promise Version
import {Injectable}              from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {User} from './user';
import {BaseService} from "./base.service";

@Injectable()
export class UserService extends BaseService{
    // URL to web api
    private usersUrl = this.baseUrl + '/api/users';

    getUsers(): Promise<User[]> {
        return this.http.get(this.usersUrl)
            .toPromise()
            .then(this.extractData)
            .catch(this.handleError);
    }

    getUser(userId: string): Promise<User> {
        return this.http.get(this.usersUrl+'/'+userId)
            .toPromise()
            .then(this.extractData)
            .catch(this.handleError);
    }

}

