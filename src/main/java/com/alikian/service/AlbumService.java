package com.alikian.service;

import com.alikian.dto.AlbumDto;
import com.alikian.dto.PhotoDto;
import com.alikian.dto.UserDto;

import java.util.List;

/**
 * Created by akian on 2/22/17.
 */
public interface AlbumService {
    void saveAll(List<AlbumDto> albumDtos);
    List<AlbumDto> getAll();

    AlbumDto getOne(Integer userId);

    AlbumDto saveOrUpdate(AlbumDto userDto);

    void delete(Integer userId);

    List<AlbumDto> getAlbumsForUser(Integer userId);

    List<PhotoDto> getPhotosForAlbum(Integer albumId);
}
