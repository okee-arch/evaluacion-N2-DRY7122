pipeline {
    agent any

    environment {
        IMAGE_NAME = 'fastapi-dolarapi'
    }

    stages {
        stage('Limpiar contenedores e imágenes anteriores') {
            steps {
                script {
                    sh '''
                    # Parar y eliminar contenedor si existe
                    if [ "$(docker ps -q -f name=${IMAGE_NAME})" ]; then
                      docker stop ${IMAGE_NAME}
                      docker rm ${IMAGE_NAME}
                    fi

                    # Eliminar imagen si existe
                    if [ "$(docker images -q ${IMAGE_NAME})" ]; then
                      docker rmi -f ${IMAGE_NAME}
                    fi
                    '''
                }
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Levantar contenedor') {
            steps {
                sh 'docker run -d -p 8000:8000 --name ${IMAGE_NAME} ${IMAGE_NAME}'
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado"
        }
    }
}
