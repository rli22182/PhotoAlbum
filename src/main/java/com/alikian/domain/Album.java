package com.alikian.domain;

import javax.persistence.*;
import java.util.List;

/**
 * Created by Ali on 2/21/2017.
 */
@Entity(name = "album")
public class Album {

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    private Long id;

    private String title;

    @ManyToOne(fetch=FetchType.LAZY)
    @JoinColumn(name="user_id")
    private User user;

    @OneToMany(mappedBy="album")
    private List<Photo> photos;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
}
