/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('build') {
            agent {
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
		        sh 'python manage.py runserver'
            }
        }
    }
}
