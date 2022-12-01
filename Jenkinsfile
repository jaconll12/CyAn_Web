    pipeline {    
        agent any
        stages {
            stage('Build') {
                steps {
                    sh '''
                    chmod +x build.sh
                    ./build.sh
                    '''
                }
            }
            

            stage('Deploy') {
                steps {
                    sh '''
                    pwd
                   
                    '''
                }
            }
        }
    }