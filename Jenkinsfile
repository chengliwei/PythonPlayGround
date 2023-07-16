pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/chengliwei/PythonPlayGround.git']])
            }
        }

        stage ('Set Properties Files Variables') {
            steps {
                script {
                    pipelinePropertiesFile = 'prod.properties'
                    echo "Reading ${pipelinePropertiesFile}"
                    PipelineProperties = readProperties(file: "$pipelinePropertiesFile")
                    coolVariable = PipelineProperties.coolVariable
                    echo "${coolVariable}"

                }
            }
        }

        stage('Run Python Script') {
            steps {
                powershell "python helloworld.py $coolVariable"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}