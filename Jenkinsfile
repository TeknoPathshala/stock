pipeline {
    agent any

    environment {
        PYTHON_EXECUTABLE = sh(script: 'which python', returnStdout: true).trim()
        PATH = "${PYTHON_EXECUTABLE%/*}:$$PATH"
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
            sh 'pkill -f "python app.py"'
        }
    }
}
