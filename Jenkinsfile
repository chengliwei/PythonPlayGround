pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/chengliwei/PythonPlayGround.git']])
            }
        }

        stage('Run Python Script') {
            steps {
                powershell 'python helloworld.py'
            }
        }
    }
}