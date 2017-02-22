package com.alikian.domain;

import javax.persistence.*;
import java.util.List;

/**
 * Created by Ali on 2/21/2017.
 */
@Entity(name = "user")
public class User {

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    private Long id;

    @OneToMany(mappedBy="user")
    private List<Album> albums;

    @Column(length = 50)
    private String name;
    @Column(length = 50)
    private String username;
    @Column(length = 50)
    private String email;

    @Column(length = 50)
    private String addressStreet;
    @Column(length = 50)
    private String addressSuite;
    @Column(length = 50)
    private String addressCity;
    @Column(length = 20)
    private String addressZipcode;
    @Column
    private Double addressGeoLat;
    @Column
    private Double addressGeoLng;

    @Column(length = 50)
    private String phone;
    @Column(length = 50)
    private String website;
    @Column(length = 50)
    private String companyName;
    @Column(length = 100)
    private String companyCatchPhrase;
    @Column(length = 100)
    private String companyBs;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getAddressStreet() {
        return addressStreet;
    }

    public void setAddressStreet(String addressStreet) {
        this.addressStreet = addressStreet;
    }

    public String getAddressSuite() {
        return addressSuite;
    }

    public void setAddressSuite(String addressSuite) {
        this.addressSuite = addressSuite;
    }

    public String getAddressCity() {
        return addressCity;
    }

    public void setAddressCity(String addressCity) {
        this.addressCity = addressCity;
    }

    public String getAddressZipcode() {
        return addressZipcode;
    }

    public void setAddressZipcode(String addressZipcode) {
        this.addressZipcode = addressZipcode;
    }

    public Double getAddressGeoLat() {
        return addressGeoLat;
    }

    public void setAddressGeoLat(Double addressGeoLat) {
        this.addressGeoLat = addressGeoLat;
    }

    public Double getAddressGeoLng() {
        return addressGeoLng;
    }

    public void setAddressGeoLng(Double addressGeoLng) {
        this.addressGeoLng = addressGeoLng;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }

    public String getCompanyName() {
        return companyName;
    }

    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }

    public String getCompanyCatchPhrase() {
        return companyCatchPhrase;
    }

    public void setCompanyCatchPhrase(String companyCatchPhrase) {
        this.companyCatchPhrase = companyCatchPhrase;
    }

    public String getCompanyBs() {
        return companyBs;
    }

    public void setCompanyBs(String companyBs) {
        this.companyBs = companyBs;
    }

    public List<Album> getAlbums() {
        return albums;
    }

    public void setAlbums(List<Album> albums) {
        this.albums = albums;
    }
}
