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
                    echo pwd
                    python3 manage.py runserver 
                    '''
                }
            }
        }
    }