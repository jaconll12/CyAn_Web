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
                    // Set both label and image
                    label 'docker'
                    image 'node:7-alpine'
                    args '--name docker-node' // list any args
                        }
                }
                steps {
    
                    sh "bash build.sh"
                
                }
            }
        }
    }
    