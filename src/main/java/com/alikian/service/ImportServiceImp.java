package com.alikian.service;

import com.alikian.dto.AlbumDto;
import com.alikian.dto.PhotoDto;
import com.alikian.dto.UserDto;
import com.alikian.repository.AlbumRepository;
import com.alikian.repository.PhotoRepository;
import com.alikian.repository.UserRepository;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.List;

/**
 * Created by akian on 2/22/17.
 */
@Service
@Transactional(propagation = Propagation.REQUIRED)
public class ImportServiceImp implements ImportService {
    private final Logger logger = LoggerFactory.getLogger(ImportService.class);

    @Autowired
    UserRepository userRepository;

    @Autowired
    AlbumRepository albumRepository;

    @Autowired
    PhotoRepository photoRepository;

    @Autowired
    UserService userService;

    @Autowired
    AlbumService albumService;

    @Autowired
    PhotoService photoService;

    @Override
    public void importData() {
        System.out.println("ContextStartedEvent Received " + userRepository.getClass());

        photoRepository.deleteAll();
        albumRepository.deleteAll();
        userRepository.deleteAll();
        logger.info("All Tables wiped out");


        ObjectMapper objectMapper = new ObjectMapper();
        try {
            BufferedReader userStream = getStream("https://jsonplaceholder.typicode.com/users");
            List<UserDto> userDtos = objectMapper.readValue(userStream, new TypeReference<List<UserDto>>() {
            });
            userStream.close();
            logger.info("Users loaded {}", userDtos.size());

            BufferedReader albumStream = getStream("https://jsonplaceholder.typicode.com/albums");
            List<AlbumDto> albumDtos = objectMapper.readValue(albumStream, new TypeReference<List<AlbumDto>>() {
            });
            albumStream.close();
            logger.info("Album loaded {}", albumDtos.size());

            BufferedReader photosStream = getStream("https://jsonplaceholder.typicode.com/photos");
            List<PhotoDto> photoDtos = objectMapper.readValue(photosStream, new TypeReference<List<PhotoDto>>() {
            });
            photosStream.close();
            logger.info("Photo loaded {}", photoDtos.size());

            userService.saveAll(userDtos);
            logger.info("Users records inserted");
            albumService.saveAll(albumDtos);
            logger.info("Albums records inserted");
            photoService.saveAll(photoDtos);
            logger.info("Photo records inserted");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    BufferedReader getStream(String urlString) throws IOException {
        URL url = null;
        url = new URL(urlString);
        BufferedReader in = new BufferedReader(
            new InputStreamReader(url.openStream()));
        return in;

    }
}
