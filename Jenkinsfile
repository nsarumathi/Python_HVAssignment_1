pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Ensure your Jenkins job configuration points to 'main' (not 'master') 
                // to avoid the Git status code 128 error.
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                echo 'Setting up virtual environment...'
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                # Only runs if requirements.txt exists
                if [ -f requirements.txt ]; then ./venv/bin/pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Test Assignment 1') {
            steps {
                echo 'Running Assignment 1...'
                sh './venv/bin/python assgmnt1.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf venv'
        }
    }
}
