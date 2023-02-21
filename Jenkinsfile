    pipeline {    
        agent any
        stages {
            stage('Build') {
                steps {
                    sh '''
                    echo "building ....."
                    '''
                }
            }
            
            stage('Test') {
                agent {
                    docker {
                        image 'python:3-alpine'
                    }
                }
                steps {
    
                    sh "bash build.sh"
                
                }
            }
        }
    }
    