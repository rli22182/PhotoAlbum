package com.alikian.service;

import com.alikian.dto.AlbumDto;

import java.util.List;

/**
 * Created by akian on 2/22/17.
 */
public interface AlbumService {
    void saveAll(List<AlbumDto> albumDtos);

    AlbumDto getOne(Integer userId);

    AlbumDto saveOrUpdate(AlbumDto userDto);

    void delete(Integer userId);

}
