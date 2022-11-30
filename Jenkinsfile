      pipeline {    
        agent any
        stages {
            stage('Build') {
                steps {
                    withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']){
                        sh 'env/bin/pip install -r requirements.txt
                    
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
