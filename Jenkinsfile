pipeline {
    agent any

    stages {
        stage('Run ansible') {
            steps {
                echo "hello"
        }
    
        stage('Build Docker Image') {
            steps {
                echo "bye"
        }

    }
    post { 
        always { 
            echo " removing container "
        }
    }
}