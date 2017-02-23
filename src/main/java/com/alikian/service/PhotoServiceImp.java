package com.alikian.service;

import com.alikian.domain.Photo;
import com.alikian.dto.PhotoDto;
import com.alikian.orika.mapper.PhotoMapper;
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

    public PhotoDto getOne(Integer albumId) {
        Photo photo = photoRepository.findOne(albumId);
        PhotoDto photoDto = photoMapper.map(photo, PhotoDto.class);

        return photoDto;
    }

    public PhotoDto saveOrUpdate(PhotoDto photoDto) {
        Photo photo = photoMapper.map(photoDto, Photo.class);

        Photo updatedPhoto = photoRepository.save(photo);

        PhotoDto updatedPhotoDto = photoMapper.map(updatedPhoto, PhotoDto.class);
        return updatedPhotoDto;
    }

    public void delete(Integer photoId) {
        photoRepository.delete(photoId);
    }

}
