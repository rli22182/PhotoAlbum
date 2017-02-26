import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent }   from './home.component';
import { UsersComponent }      from './users.component';
import { AlbumsComponent }  from './albums.component';

const routes: Routes = [
    { path: '', component: UsersComponent },
    { path: 'home',  component: HomeComponent },
    { path: 'users/:id', component: AlbumsComponent },
    { path: 'users',     component: UsersComponent }
];

@NgModule({
    imports: [ RouterModule.forRoot(routes) ],
    exports: [ RouterModule ]
})
export class AppRoutingModule {}