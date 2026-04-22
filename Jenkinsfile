pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                echo 'Setting up virtual environment and dependencies...'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Parallel Assignment Testing') {
            parallel {
                stage('Test Assignment 1') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python assgmnt1.py
                        '''
                    }
                }

                stage('Test Assignment 2') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python assgmnt2.py
                        '''
                    }
                }

                stage('Test Assignment 3') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python assgmnt3.py
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            // Optional: remove the virtual env to save space
            sh 'rm -rf venv'
        }
    }
}
