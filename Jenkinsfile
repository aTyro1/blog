pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                
                sh 'docker-compose up --build -d'
                echo 'docker-compose build image completed'
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