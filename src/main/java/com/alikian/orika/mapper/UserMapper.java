package com.alikian.orika.mapper;

import com.alikian.domain.User;
import com.alikian.dto.UserDto;
import ma.glasnost.orika.MapperFactory;
import ma.glasnost.orika.impl.ConfigurableMapper;
import org.springframework.stereotype.Component;

/**
 * Created by Ali on 2/21/2017.
 */
@Component
public class UserMapper extends ConfigurableMapper {
    protected void configure(MapperFactory factory) {
        factory.classMap(User.class, UserDto.class)
                .field("addressStreet", "address.street")
                .field("addressSuite", "address.suite")
                .field("addressCity", "address.city")
                .field("addressZipcode", "address.zipcode")
                .field("addressGeoLat", "address.geo.lat")
                .field("addressGeoLng", "address.geo.lng")
                .field("companyName", "company.name")
                .field("companyCatchPhrase", "company.catchPhrase")
                .field("companyBs", "company.bs")
                .byDefault()
                .register();

    }
}
