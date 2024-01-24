pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                
                echo "building"
               
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