    pipeline {    
        agent any
        stages {
            stage('Build') {
                steps {
    
                    sh "build.sh"
                
                }
            }
            
            stage('Test') {
        
                steps {
    
                    sh "test.sh"
                
                }
                stage('Deploy') {
        
                steps {
    
                    sh "deploy.sh"
                
                }
            }
        }
    }
    