    pipeline {    
        agent { docker { image 'python:3.7.2' } }
        stages {
            stage('Build') {
                steps {
                    sh 'pip install -r requirements.txt'
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