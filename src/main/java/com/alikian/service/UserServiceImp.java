package com.alikian.service;

import com.alikian.domain.User;
import com.alikian.dto.UserDto;
import com.alikian.orika.mapper.UserMapper;
import com.alikian.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 * Created by akian on 2/22/17.
 */
@Service
@Transactional(propagation = Propagation.REQUIRED)
public class UserServiceImp implements UserService {

    @Autowired
    UserRepository userRepository;

    @Autowired
    UserMapper userMapper;

    @Override
    public void saveAll(List<UserDto> userDtos) {
        List<User> users = userMapper.mapAsList(userDtos, User.class);

        userRepository.save(users);
    }
}
