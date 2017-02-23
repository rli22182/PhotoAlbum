package com.alikian.service;

import com.alikian.dto.AlbumDto;
import com.alikian.dto.PhotoDto;

import java.util.List;

/**
 * Created by akian on 2/22/17.
 */
public interface PhotoService {
    void saveAll(List<PhotoDto> photoDtos);
}
