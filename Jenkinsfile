pipeline {
    agent any

    tools {
        python 'python3' // Replace 'python3' with the Python installation label configured in Jenkins
    }

    stages {
        stage('version') {
            steps {
                bat 'python --version'
            }
        }
    }
}