var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component } from '@angular/core';
import { UserService } from './user.service';
export var AppComponent = (function () {
    function AppComponent(userService) {
        this.userService = userService;
        this.title = 'Photo Album';
    }
    AppComponent.prototype.onSelect = function (user) {
        this.selectedUser = user;
    };
    AppComponent.prototype.ngOnInit = function () {
        this.getUsers();
    };
    AppComponent.prototype.getUsers = function () {
        var _this = this;
        this.userService.getUsers()
            .then(function (users) { return _this.users = users; }, function (error) { return _this.errorMessage = error; });
    };
    AppComponent = __decorate([
        Component({
            selector: 'app-root',
            templateUrl: './app.component.html',
            styleUrls: ['./app.component.css'],
            template: "\n  <div style=\"width: 100%; overflow: hidden;\">\n<div style=\"width: 400px; float: left;\">\n<ul class=\"users\">\n<li *ngFor=\"let user of users\"\n[class.selected]=\"user === selectedUser\"\n(click)=\"onSelect(user)\">\n\n    <!-- each user goes here -->\n    <span class=\"badge\">{{user.id}}</span> {{user.name}}\n  </li>\n</ul>\n</div>\n<div style=\"margin-left: 420px;\" *ngIf=\"selectedUser\">\n  <h2>{{selectedUser.name}}</h2>\n  <div><label>id: </label>{{selectedUser.id}}</div>\n  <div>\n    <label>name: </label>\n    <input [(ngModel)]=\"selectedUser.name\" placeholder=\"name\"/>\n  </div>\n  <div>\n    <label>username: </label>\n    <input [(ngModel)]=\"selectedUser.username\" placeholder=\"username\"/>\n  </div>\n  <div>\n    <label>email: </label>\n    <input [(ngModel)]=\"selectedUser.email\" placeholder=\"email\"/>\n  </div>\n  <div>\n  <h3>Address</h3>\n  <div>\n    <label>street: </label>\n    <label> {{selectedUser.address.street}} </label>\n  </div>\n  <div>\n    <label>suite: </label>\n    <label> {{selectedUser.address.suite}} </label>\n  </div>\n  <div>\n    <label>city: </label>\n    <label> {{selectedUser.address.city}} </label>\n  </div>\n  <div>\n    <label>zipcode: </label>\n    <label> {{selectedUser.address.zipcode}} </label>\n  </div>\n  </div>\n</div>\n</div>\n  ",
            providers: [UserService]
        }), 
        __metadata('design:paramtypes', [UserService])
    ], AppComponent);
    return AppComponent;
}());
//# sourceMappingURL=/Users/akian/PhotoAlbum/src/main/front/src/app/app.component.js.map