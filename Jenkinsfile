pipeline {
    agent any

    stages {
        stage('Unit Test and dockerization') {
            steps {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh './build.sh'
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