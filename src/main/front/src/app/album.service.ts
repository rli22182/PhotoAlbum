import {Injectable}              from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {Album} from './album';
import {BaseService} from "./base.service";

@Injectable()
export class AlbumService extends BaseService{
    // URL to web api
    private albumsUrl = this.baseUrl + '/api/users/userId/albums';

    getUserAlbums(userId: string): Promise<Album[]> {
        return this.http.get(this.albumsUrl.replace(/userId/gi,userId))
            .toPromise()
            .then(this.extractData)
            .catch(this.handleError);
    }

}

