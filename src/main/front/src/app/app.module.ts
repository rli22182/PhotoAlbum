import {NgModule}       from '@angular/core';
import {BrowserModule}  from '@angular/platform-browser';
import {FormsModule}    from '@angular/forms';
import {HttpModule, JsonpModule} from '@angular/http';

import {AppComponent}         from './app.component';
import {AlbumsComponent}  from './albums.component';
import {UsersComponent}       from './users.component';
import {UserService}          from './user.service';

import {AppRoutingModule}     from './app-routing.module';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        AppRoutingModule,
        HttpModule
    ],
    declarations: [
        AppComponent,
        AlbumsComponent,
        UsersComponent
    ],
    providers: [UserService],
    bootstrap: [AppComponent]
})
export class AppModule {
}