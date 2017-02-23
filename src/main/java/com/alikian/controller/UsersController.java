package com.alikian.controller;

import com.alikian.domain.User;
import com.alikian.dto.UserDto;
import com.alikian.orika.mapper.UserMapper;
import com.alikian.repository.UserRepository;
import com.alikian.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Created by Ali on 2/21/2017.
 */
@RestController
public class UsersController {

    @Autowired
    UserService userService;

    @RequestMapping(value = "/users",method = RequestMethod.GET)
    public List<UserDto> getAll() {
        return userService.getAll();
    }

    @RequestMapping(value = "/users/{id}",method = RequestMethod.GET)
    public UserDto getOne(@PathVariable("id") Integer userId) {
        return userService.getOne(userId);
    }

    @RequestMapping(value = "/users",method = RequestMethod.PUT)
    public UserDto update(@RequestBody  UserDto userDto) {
        return userService.saveOrUpdate(userDto);
    }

    @RequestMapping(value = "/users",method = RequestMethod.POST)
    public UserDto save(@RequestBody  UserDto userDto) {
        return userService.saveOrUpdate(userDto);
    }

    @RequestMapping(value = "/users/{id}",method = RequestMethod.DELETE)
    public void delete(@PathVariable("id") Integer id) {
        userService.delete(id);
    }

}
