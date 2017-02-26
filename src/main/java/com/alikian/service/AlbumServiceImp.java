package com.alikian.service;

import com.alikian.domain.Album;
import com.alikian.domain.Photo;
import com.alikian.domain.User;
import com.alikian.dto.AlbumDto;
import com.alikian.dto.PhotoDto;
import com.alikian.dto.UserDto;
import com.alikian.orika.mapper.AlbumMapper;
import com.alikian.orika.mapper.PhotoMapper;
import com.alikian.orika.mapper.UserMapper;
import com.alikian.repository.AlbumRepository;
import com.alikian.repository.PhotoRepository;
import com.alikian.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
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
    PhotoRepository photoRepository;

    @Autowired
    AlbumMapper albumMapper;

    @Autowired
    PhotoMapper photoMapper;

    @Override
    public void saveAll(List<AlbumDto> albumDtos) {
        List<Album> albums = albumMapper.mapAsList(albumDtos, Album.class);

        albumRepository.save(albums);
    }

    public List<AlbumDto> getAll() {
        Iterable<Album> albumIterable = albumRepository.findAll();
        List<Album> albums = new ArrayList<>();
        albumIterable.forEach(albums::add);
        List<AlbumDto> albumDtos = albumMapper.mapAsList(albums, AlbumDto.class);
        return albumDtos;
    }

    public AlbumDto getOne(Integer albumId) {
        Album album = albumRepository.findOne(albumId);
        AlbumDto albumDto = albumMapper.map(album, AlbumDto.class);

        return albumDto;
    }

    public AlbumDto saveOrUpdate(AlbumDto albumDto) {
        Album album = albumMapper.map(albumDto, Album.class);

        Album updatedAlbum = albumRepository.save(album);

        AlbumDto updatedAlbumDto = albumMapper.map(updatedAlbum, AlbumDto.class);
        return updatedAlbumDto;
    }

    public void delete(Integer albumId) {
        albumRepository.delete(albumId);
    }

    @Override
    public List<AlbumDto> getAlbumsForUser(Integer userId) {
        List<Album> albumList =  albumRepository.findByUser_id(userId);
        List<AlbumDto> albumDtos = albumMapper.mapAsList(albumList, AlbumDto.class);
        return albumDtos;
    }

    @Override
    public List<PhotoDto> getPhotosForAlbum(Integer albumId) {
        List<Photo> photos = photoRepository.findByAlbum_id(albumId);
        return photoMapper.mapAsList(photos,PhotoDto.class);
    }


}
