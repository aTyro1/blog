pipeline {
    agent any

    stages {
        stage('Unit Testing') {
            steps {
                sh "python3 manage.py test writers"
            }
        }
        stage('Making WSGI using GUNICORN'){
            steps{
                sh 'docker build .'
            }
        }
        stage('Builiding NGINX reverse PROXY and Load Testing using locust ')
        {
            steps{

                sh 'docker-compose up --build -d'
                sh './loadlog.sh'

            }
        }

    }

    post {
        success {
            echo "Build successful"
        }

        failure {
            echo "Build failed"
        }
    }
}