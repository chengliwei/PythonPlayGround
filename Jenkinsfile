pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage ('Set Properties Files Variables') {
            steps {
                script {
                    pipelinePropertiesFile = 'prod.properties'
                    echo "Reading ${pipelinePropertiesFile}"
                    PipelineProperties = readProperties(file: "$pipelinePropertiesFile")
                    coolVariable = PipelineProperties.coolVariable
                    radVariable = PipelineProperties.radVariable
                    adminEmail = PipelineProperties.adminEmail
                    //echo "${coolVariable}"

                }
            }
        }

        stage('Run Python Script') {
            steps {
                powershell "python helloworld.py $coolVariable $radVariable $adminEmail"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}