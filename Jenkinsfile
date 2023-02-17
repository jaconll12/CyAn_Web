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
            
            stage('Test') {
                steps {
                    sh '''
                    python3 -m venv env
                    source env/bin/activate
                    pip install --upgrade pip
                    pip3 install -r requirements.txt

                    python manage.py migrate
                    python manage.py test
                    '''
                }
            }
        }
    }
    