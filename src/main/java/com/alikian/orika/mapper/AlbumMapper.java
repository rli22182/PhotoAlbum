package com.alikian.orika.mapper;

import com.alikian.domain.Album;
import com.alikian.domain.User;
import com.alikian.dto.AlbumDto;
import com.alikian.dto.UserDto;
import ma.glasnost.orika.MapperFactory;
import ma.glasnost.orika.impl.ConfigurableMapper;
import org.springframework.stereotype.Component;

/**
 * Created by Ali on 2/21/2017.
 */
@Component
public class AlbumMapper extends ConfigurableMapper {
    protected void configure(MapperFactory factory) {
        factory.classMap(Album.class, AlbumDto.class)
                .field("user.id", "userId")
                .byDefault()
                .register();

    }
}
