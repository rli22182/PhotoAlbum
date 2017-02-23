package com.alikian.controller;

import com.alikian.dto.AlbumDto;
import com.alikian.service.AlbumService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * Created by Ali on 2/21/2017.
 */
@RestController
public class AlbumsController {

    @Autowired
    AlbumService albumService;

    @RequestMapping(value = "/albums/{id}",method = RequestMethod.GET)
    public AlbumDto getOne(@PathVariable("id") Integer userId) {
        return albumService.getOne(userId);
    }

    @RequestMapping(value = "/albums",method = RequestMethod.PUT)
    public AlbumDto update(@RequestBody  AlbumDto albumDto) {
        return albumService.saveOrUpdate(albumDto);
    }

    @RequestMapping(value = "/albums",method = RequestMethod.POST)
    public AlbumDto save(@RequestBody  AlbumDto albumDto) {
        return albumService.saveOrUpdate(albumDto);
    }

    @RequestMapping(value = "/albums/{id}",method = RequestMethod.DELETE)
    public void delete(@PathVariable("id") Integer id) {
        albumService.delete(id);
    }

}
