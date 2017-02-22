package com.alikian.controller;

import com.alikian.domain.User;
import com.alikian.dto.UserDto;
import com.alikian.orika.mapper.UserMapper;
import com.alikian.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * Created by Ali on 2/21/2017.
 */
@RestController
public class UsersController {

    @Autowired
    UserRepository userRepository;

    @Autowired
    UserMapper userMapper;

    @RequestMapping(value = "/users/{id}",method = RequestMethod.GET)
    public UserDto getOne(@PathVariable("id") Long id) {
        User user=userRepository.findOne(id);
        UserDto userDto = userMapper.map(user, UserDto.class);

        return userDto;
    }

    @RequestMapping(value = "/users",method = RequestMethod.PUT)
    public UserDto update(@RequestBody  UserDto userDto) {
        return saveOrUpdate(userDto);
    }

    @RequestMapping(value = "/users",method = RequestMethod.POST)
    public UserDto save(@RequestBody  UserDto userDto) {
        return saveOrUpdate(userDto);
    }

    @RequestMapping(value = "/users/{id}",method = RequestMethod.DELETE)
    public void delete(@PathVariable("id") Long id) {
        userRepository.delete(id);
    }

    private UserDto saveOrUpdate(UserDto userDto){
        User user = userMapper.map(userDto, User.class);

        User updatedUser = userRepository.save(user);

        UserDto updatedUserDto = userMapper.map(updatedUser, UserDto.class);
        return updatedUserDto;
    }
}
