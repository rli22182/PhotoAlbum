package com.alikian.controller;

import com.alikian.dto.PhotoDto;
import com.alikian.service.AlbumService;
import com.alikian.service.PhotoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * Created by Ali on 2/21/2017.
 */
@RestController
public class PhotosController {

    @Autowired
    PhotoService photoService;

    @RequestMapping(value = "/photos/{id}",method = RequestMethod.GET)
    public PhotoDto getOne(@PathVariable("id") Integer userId) {
        return photoService.getOne(userId);
    }

    @RequestMapping(value = "/photos",method = RequestMethod.PUT)
    public PhotoDto update(@RequestBody  PhotoDto photoDto) {
        return photoService.saveOrUpdate(photoDto);
    }

    @RequestMapping(value = "/photos",method = RequestMethod.POST)
    public PhotoDto save(@RequestBody  PhotoDto photoDto) {
        return photoService.saveOrUpdate(photoDto);
    }

    @RequestMapping(value = "/photos/{id}",method = RequestMethod.DELETE)
    public void delete(@PathVariable("id") Integer id) {
        photoService.delete(id);
    }

}
