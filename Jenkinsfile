pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']], 
                          userRemoteConfigs: [[url: 'https://github.com/TeknoPathshala/stock.git']]])
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
