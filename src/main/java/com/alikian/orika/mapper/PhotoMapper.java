package com.alikian.orika.mapper;

import com.alikian.domain.Album;
import com.alikian.domain.Photo;
import com.alikian.dto.AlbumDto;
import com.alikian.dto.PhotoDto;
import ma.glasnost.orika.MapperFactory;
import ma.glasnost.orika.impl.ConfigurableMapper;
import org.springframework.stereotype.Component;

/**
 * Created by Ali on 2/21/2017.
 */
@Component
public class PhotoMapper extends ConfigurableMapper {
    protected void configure(MapperFactory factory) {
        factory.classMap(Photo.class, PhotoDto.class)
                .field("album.id", "albumId")
                .byDefault()
                .register();

    }
}
