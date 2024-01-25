pipeline {
    agent any

    stages {
        stage('Dockerization'){
            steps{
                sh 'docker-compose up --build -d'
            }
        }

    }

    post {
        success {
            echo "Build successful"
            // You can add additional steps here, like running tests or notifications.
        }

        failure {
            echo "Build failed"
        }
    }
}