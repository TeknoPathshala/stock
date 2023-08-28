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
                def APP_PID_FILE = 'app.pid'
                
                try {
                    echo "Reading PID from file..."
                    def pid = readFile("${APP_PID_FILE}").trim()
                    echo "Killing process with PID: ${pid}"
                    sh "pkill -9 -F ${APP_PID_FILE}"
                    echo "Process killed successfully"
                } catch (Exception e) {
                    echo "Error reading or killing process: ${e.message}"
                }
            }
        }
    }
}
