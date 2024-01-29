pipeline {
    agent any

    stages {
        stage('Unit Testing') {
            steps {
                sh "python3 manage.py test blogs"
                sh "python3 manage.py test writers"
            }
        }
        stage('Making WSGI using GUNICORN'){
            steps{
                sh 'docker build .'
            }
        }
        stage('Builiding NGINX reverse PROXY ')
        {
            steps{

                sh 'docker-compose up --build -d'
            }
        }

    }

    post {
        stage('Performance Testing')
        {
            steps{

                sh 'locust -f locustfile.py -H http://0.0.0.0 -u 1000 -r 10 -t 300s --autostart --autoexit --csv "stats/" '

            }
        }

        success {
            echo "Build successful"
        }

        failure {
            echo "Build failed"
        }
    }
}