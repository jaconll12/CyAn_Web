      pipeline {    
        agent {
            withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']){
                docker { image 'node:16.13.1-alpine' }
            }
        }
        stages {
            stage('Build') {
                steps {
                    withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']){
                        sh 'bin/pip install -r requirements.txt'
                    
                    }
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
