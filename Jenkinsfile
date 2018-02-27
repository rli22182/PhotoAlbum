pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('StartService') {
            steps {
                sh 'java -jar target/photoalbum-0.0.1-SNAPSHOT.jar &'
            }
        }
        stage('TestService') {
            steps {
                sh 'python test/TestCases/UserTestCases.py'
                sh 'python test/TestCases/AlbumTestCases.py'
                sh 'python test/TestCases/PhotoTestCases.py'
            }
        }
        stage('TearDown') {
            steps {
                sh 'pkill -f photoalbum'
            }
        }
    }
}
