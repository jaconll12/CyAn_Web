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
                steps {
    
                    sh "bash build.sh"
                
                }
            }
        }
    }
    