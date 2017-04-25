package com.alikian.controller;

import com.alikian.dto.AlbumDto;
import com.alikian.dto.PhotoDto;
import com.alikian.dto.UserDto;
import com.alikian.service.AlbumService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Created by Ali on 2/21/2017.
 */
@RestController
@CrossOrigin
@RequestMapping(value = Path.API+"/albums")
public class AlbumsController {

    @Autowired
    AlbumService albumService;

    @RequestMapping(method = RequestMethod.GET)
    public List<AlbumDto> getAll() {
        return albumService.getAll();
    }

    @RequestMapping(value = "/{id}/photos",method = RequestMethod.GET)
    public List<PhotoDto> getUserAlbums(@PathVariable("id")Integer albumId){
        return albumService.getPhotosForAlbum(albumId);
    }

    @RequestMapping(value = "/{id}",method = RequestMethod.GET)
    public AlbumDto getOne(@PathVariable("id") Integer userId) {
        return albumService.getOne(userId);
    }

    @RequestMapping(method = RequestMethod.PUT)
    public AlbumDto update(@RequestBody  AlbumDto albumDto) {
        return albumService.saveOrUpdate(albumDto);
    }

    @RequestMapping(method = RequestMethod.POST)
    public AlbumDto save(@RequestBody  AlbumDto albumDto) {
        return albumService.saveOrUpdate(albumDto);
    }

    @RequestMapping(value = "/{id}",method = RequestMethod.DELETE)
    public void delete(@PathVariable("id") Integer id) {
        albumService.delete(id);
    }

}
