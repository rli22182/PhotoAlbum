// Promise Version
import {Injectable}              from '@angular/core';
import {Http, Response}          from '@angular/http';
import {Headers, RequestOptions} from '@angular/http';

import 'rxjs/add/operator/toPromise';

import {User} from './user';

@Injectable()
export class UserService {
    // URL to web api
    private usersUrl = 'http://localhost:8090/api/users/{userId}/albums';
    // private albumsUrl = '/api/users/{userId}/albums';

    constructor(private http: Http) {
    }

    getUserAlbums(userId: string): Promise<User[]> {
        return this.http.get(this.albumsUrl.replace(/userId/gi,userId))
            .toPromise()
            .then(this.extractData)
            .catch(this.handleError);
    }


    private extractData(res: Response) {
        let body = res.json();
        console.log(body);
        return body || {};
    }

    private handleError(error: Response | any) {
        // In a real world app, we might use a remote logging infrastructure
        let errMsg: string;
        if (error instanceof Response) {
            const body = error.json() || '';
            const err = body.error || JSON.stringify(body);
            errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
        } else {
            errMsg = error.message ? error.message : error.toString();
        }
        console.error(errMsg);
        return Promise.reject(errMsg);
    }

}


/*
 Copyright 2017 Google Inc. All Rights Reserved.
 Use of this source code is governed by an MIT-style license that
 can be found in the LICENSE file at http://angular.io/license
 */
