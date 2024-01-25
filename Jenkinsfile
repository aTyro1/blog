pipeline {
    agent any

    stages {
        stage('Unit Testing') {
            steps {
                sh "python3 manage.py test blogs"
                sh "python3 manage.py test writers"
            }
        }
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