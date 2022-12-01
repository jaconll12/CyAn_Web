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
            

            stage('Test') {
                steps {
                    withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']){
                        sh 'echo "Test not yet..."'
                    }
                }
            }

            stage('Deploy') {
                steps {
                    withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']){
                        sh 'echo "Deploy not yet..."'
                    }
                }
            }
        }
    }