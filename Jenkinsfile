    pipeline {    
        agent any
        stages {
            stage('Build') {
                steps {
                    sh "bash build.sh"
                
                }
            }
            
            stage('Test') {
        
                steps {
    
                    sh "bash test.sh"
                
                }
                
            }
            stage('Deploy') {
        
                steps {
    
                    sh "bash deploy.sh"
                
                }
                
            }
        }
    }
    