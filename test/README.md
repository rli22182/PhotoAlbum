# Testing the PhotoAlbum Project

Testing code for the PhotoAlbum project

### Prerequisites

Python 2.7
JDK
Maven

## Running the tests

Open Terminal, navigate to your target folder to store the project files
```
$ git clone https://github.com/rli22182/PhotoAlbum.git
$ cd PhotoAlbum
$ mvn clean package
$ java -jar target/photoalbum-0.0.1-SNAPSHOT.jar
```
Check the PhotoAlbum service is accessible via URL http://localhost:8080, or http://<your_machine_ip>:8080
Update the baseURL in PhotoAlbum/test/TestCases/config.json
```
$ python test/TestCases/UserTestCases.py
$ python test/TestCases/AlbumTestCases.py
$ python test/TestCases/PhotoTestCases.py
```
Test log files will be generated under the TestCases folder with SUCCESS/ERROR info

### Known failed cases

Some issues found during the API integration test:

* Call usersCreate API (POST /api/users) with specific User ID which does not exist in system - If the ID existed before but got deleted, then the ID cannot be re-used any more. User will be created with a system-assigned ID instead of the specified ID. However API does not return error.
* Call usersCreate API (POST /api/users) with specific ID which already exists in system - API does not return error.
* Call userUpdate API (PUT /api/users) with specific User ID which does not exist in system - API does not return error. Instead a new user will be created.
* Call albumsCreate API (POST /api/albums) without specifying Album ID and User ID - Album can be created but not associated with any user.
* Call albumsCreate API (POST /api/albums) with specific Album ID which does not exist in system - If the ID existed before but got deleted, then the ID cannot be re-used any more. Album will be created with a system-assigned ID instead of the specified ID. However API does not return error.
* Call albumsCreate API (POST /api/albums) with specific ID which already exists in system - API does not return error.
* Call albumsGetOne API (GET /api/albums{id}) with specific ID which does not exist in system - API does not return error.
* Call albumsUpdate API (PUT /api/albums) with specific ID which does not exist in system - API does not return error. Instead a new album will be created.
* /api/photos does not support GET method to get all photos.
* Call photosCreate API (POST /api/photos) without specifying Photo ID and Album ID - Photo can be created but not associated with any album.
* Call photosGetOne API (GET /api/photos{id}) with specific ID which does not exist in system - API does not return error.
* Call photosUpdate API (PUT /api/photos) with specific ID which does not exist in system - API does not return error. Instead a new photo will be created.
* Call photosCreate API (POST /api/photos) with specific Photo ID which does not exist in system - If the ID existed before but got deleted, then the ID cannot be re-used any more. Photo will be created with a system-assigned ID instead of the specified ID. However API does not return error.
* Call photosCreate API (POST /api/photos) with specific ID which already exists in system - API does not return error.
