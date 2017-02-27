import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { UsersComponent }      from './users.component';
import { AlbumsComponent }  from './albums.component';

const routes: Routes = [
    { path: '', component: UsersComponent },
    { path: 'users/:id', component: AlbumsComponent },
    { path: 'users',     component: UsersComponent }
];

@NgModule({
    imports: [ RouterModule.forRoot(routes) ],
    exports: [ RouterModule ]
})
export class AppRoutingModule {}