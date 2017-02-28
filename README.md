#Photo Album
Database Server: MySQL on localhost port 3306

## Database
database: photo_album 
username: photo
password: album123

## Build
Use following command to build jar file (maven 3 or higher required): 
mvn clean install

## run
Use following command to run: 
java -jar target/photoalbum-0.0.1-SNAPSHOT.jar

At startup application will create tables and also download data

Open browser at:
http://localhost:8080/

