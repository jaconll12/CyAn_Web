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
    
                    sh "test.sh"
                
                }
                
            }
            stage('Deploy') {
        
                steps {
    
                    sh "deploy.sh"
                
                }
                
            }
        }
    }
    