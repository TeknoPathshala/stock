pipeline {
    agent any

    environment {
        PYTHON_EXECUTABLE = sh(script: 'which python', returnStdout: true).trim()
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
                sh 'pip install -r requirements.txt'
                sh 'python app.py &'
            }
        }
    }

    post {
        always {
            node {
                sh 'pkill -f "python app.py"'
            }
        }
    }
}
