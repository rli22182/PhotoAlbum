package com.alikian.repository;

import com.alikian.domain.Album;
import com.alikian.domain.Photo;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

/**
 * Created by Ali on 2/21/2017.
 */
public interface PhotoRepository extends CrudRepository<Photo, Integer> {
    List<Photo> findByAlbum_id(Integer albumId);
}
