package com.alikian.service;

import com.alikian.domain.Album;
import com.alikian.domain.Photo;
import com.alikian.dto.AlbumDto;
import com.alikian.dto.PhotoDto;
import com.alikian.orika.mapper.AlbumMapper;
import com.alikian.orika.mapper.PhotoMapper;
import com.alikian.repository.AlbumRepository;
import com.alikian.repository.PhotoRepository;
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
public class PhotoServiceImp implements PhotoService {

    @Autowired
    PhotoRepository photoRepository;

    @Autowired
    PhotoMapper photoMapper;

    @Override
    public void saveAll(List<PhotoDto> photoDtos) {
        List<Photo> photos = photoMapper.mapAsList(photoDtos, Photo.class);

        photoRepository.save(photos);
    }
}
