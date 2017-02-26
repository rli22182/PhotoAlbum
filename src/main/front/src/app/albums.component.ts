import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Params} from '@angular/router';
import {Location}               from '@angular/common';

import {UserService} from './user.service';
import {AlbumService} from './album.service';
import {PhotoService} from './photo.service';
import {Album} from './album';
import {User} from './user';
import {Photo} from "./photo";

@Component({
    selector: 'albums',
    templateUrl: './albums.component.html',
    styleUrls: ['./albums.component.css'],
    providers: [AlbumService, PhotoService]

})
export class AlbumsComponent implements OnInit {
    title = 'Albums';
    selectedAlbum: Album;
    selectedPhoto: Photo;
    errorMessage: string;
    albums: Album[];
    photos: Photo[];
    user: User;

    constructor(private userService: UserService,
                private albumService: AlbumService,
                private photoService: PhotoService,
                private route: ActivatedRoute,
                private location: Location) {
    }

    onSelectAlbum(album: Album) {
        this.selectedAlbum = album;
        this.selectedPhoto = null;
        this.photoService.getAlbumPhotos(''+this.selectedAlbum.id).then(photos => this.photos = photos);
    }
    onSelectPhoto(photo: Photo) {
        this.selectedPhoto = photo;
    }

    onDeleteSelectPhoto() {

        this.photoService.deletePhoto(''+this.selectedPhoto.id).then(any => this.removeFromPhotos());

    }
    removeFromPhotos(){
        var index = this.photos.indexOf(this.selectedPhoto, 0);
        if (index > -1) {
            this.photos.splice(index, 1);
        }
        this.selectedPhoto = null;

    }

    ngOnInit() {
        this.route.params
            .subscribe((params: Params) => {
                this.albumService.getUserAlbums(params['id']).then(albums => this.albums = albums);
                this.userService.getUser(params['id']).then(user => this.user = user);
            });

    }

    goBack(): void {
        this.location.back();
    }

}
