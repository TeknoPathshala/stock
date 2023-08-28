pipeline {
    agent any

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
                def PYTHON_EXECUTABLE = sh(script: 'which python', returnStdout: true).trim()
                def APP_PID_FILE = 'app.pid'
                def pid = readFile("${APP_PID_FILE}").trim()
                sh "kill -9 ${pid}"
            }
        }
    }
}
