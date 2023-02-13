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
            
            stage('Deploy') {
                steps {
                    sh '''
                    chmod +x deploy.sh
                    ./deploy.sh
                    '''
                }
            }
        }
    }
    