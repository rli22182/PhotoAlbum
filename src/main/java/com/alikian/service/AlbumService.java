package com.alikian.service;

import com.alikian.dto.AlbumDto;
import com.alikian.dto.UserDto;

import java.util.List;

/**
 * Created by akian on 2/22/17.
 */
public interface AlbumService {
    void saveAll(List<AlbumDto> albumDtos);
}
