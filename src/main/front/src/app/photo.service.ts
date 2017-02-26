// Promise Version
import {Injectable}              from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {Photo} from "./photo";
import {BaseService} from "./base.service";

@Injectable()
export class PhotoService extends BaseService{
    // URL to web api
    private albumsUrl = this.baseUrl + '/api/albums/albumId/photos';
    private photoUrl =  this.baseUrl + '/api/photos';
    // private albumsUrl = '/api/albums/albumId/photos';

    getAlbumPhotos(albumId: string): Promise<Photo[]> {
        return this.http.get(this.albumsUrl.replace(/albumId/gi,albumId))
            .toPromise()
            .then(this.extractData)
            .catch(this.handleError);
    }

    deletePhoto(photoId: string): Promise<any> {
        console.log('delete photoId: ', photoId);
        return this.http.delete(this.photoUrl+'/'+photoId)
            .toPromise()
            .catch(this.handleError);
    }

}
