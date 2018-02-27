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
                sh 'photoalbum.sh start'
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
                sh 'photoalbum.sh stop'
            }
        }
    }
}
