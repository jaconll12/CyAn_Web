      pipeline {
        agent {
            docker { image 'python:3.9' }
        }
        stages {
            stage('Build') {
                steps {
                    sh 'pip install -r requirements.txt'
                }
            }

            stage('Test') {
                steps {
                    sh 'python CyAn_Web/manage.py test ./CyAn_Web'
                }
            }

            stage('Deploy') {
                steps {
                    sh 'echo not yet...'
                }
            }
        }
    }