pipeline {
    agent any

    environment {
        PYTHON_EXECUTABLE = sh(script: 'which python3', returnStdout: true).trim()
        PATH = "${PYTHON_EXECUTABLE}:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Deploy') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 app.py & echo $! > app.pid'
            }
        }
    }

    post {
        always {
            script {
                def appPidFile = readFile('app.pid').trim()
                if (appPidFile) {
                    sh "pkill -F $appPidFile"
                }
            }
        }
    }
}
