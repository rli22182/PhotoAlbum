package com.alikian.service;

import com.alikian.domain.Album;
import com.alikian.domain.User;
import com.alikian.dto.AlbumDto;
import com.alikian.dto.UserDto;
import com.alikian.orika.mapper.AlbumMapper;
import com.alikian.orika.mapper.UserMapper;
import com.alikian.repository.AlbumRepository;
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
public class AlbumServiceImp implements AlbumService {

    @Autowired
    AlbumRepository albumRepository;

    @Autowired
    AlbumMapper albumMapper;

    @Override
    public void saveAll(List<AlbumDto> albumDtos) {
        List<Album> albums = albumMapper.mapAsList(albumDtos, Album.class);

//        albums.forEach(album -> {
//            System.out.println("Album: "+album.getId());
//            albumRepository.save(album);
//        });
        albumRepository.save(albums);
    }
}
