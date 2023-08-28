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
            script {
                def processes = sh(script: "pgrep -f 'python app.py'", returnStdout: true).trim()
                sh "kill -9 ${processes}"
            }
        }
    }
}
