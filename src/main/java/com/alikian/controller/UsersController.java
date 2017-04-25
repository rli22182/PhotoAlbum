package com.alikian.controller;

import com.alikian.dto.AlbumDto;
import com.alikian.dto.UserDto;
import com.alikian.service.AlbumService;
import com.alikian.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.HttpClientErrorException;

import java.util.List;

/**
 * Created by Ali on 2/21/2017.
 */
@CrossOrigin
@RestController
@RequestMapping(value = Path.API+"/users")
public class UsersController {

    @Autowired
    UserService userService;

    @Autowired
    AlbumService albumService;

    @RequestMapping(method = RequestMethod.GET)
    public List<UserDto> getAll() {
        return userService.getAll();
    }

    @RequestMapping(value = "/{id}/albums",method = RequestMethod.GET)
    public List<AlbumDto> getUserAlbums(@PathVariable("id")Integer userId){
        return albumService.getAlbumsForUser(userId);
    }

    @RequestMapping(value = "/{id}",method = RequestMethod.GET)
    public ResponseEntity<UserDto> getOne(@PathVariable("id") Integer userId) {
        UserDto userDto = userService.getOne(userId);
        if(userDto == null){
            return new ResponseEntity<UserDto>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<UserDto>(userDto, HttpStatus.OK);
    }

    @RequestMapping(method = RequestMethod.PUT)
    public UserDto update(@RequestBody  UserDto userDto) {
        return userService.saveOrUpdate(userDto);
    }

    @RequestMapping(method = RequestMethod.POST)
    public UserDto save(@RequestBody  UserDto userDto) {
        return userService.saveOrUpdate(userDto);
    }

    @RequestMapping(value = "/{id}",method = RequestMethod.DELETE)
    public void delete(@PathVariable("id") Integer id) {
        userService.delete(id);
    }

}
