package com.alikian.repository;

import com.alikian.domain.Album;
import com.alikian.domain.User;
import org.springframework.data.repository.CrudRepository;

/**
 * Created by Ali on 2/21/2017.
 */
public interface AlbumRepository extends CrudRepository<Album, Long> {
}
