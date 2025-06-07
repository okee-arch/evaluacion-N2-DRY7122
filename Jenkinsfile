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
                    # Eliminar contenedor si existe (activo o detenido)
                    docker ps -aq -f name=${IMAGE_NAME} | xargs -r docker rm -f

                    # Eliminar imagen si existe
                    docker images -q ${IMAGE_NAME} | xargs -r docker rmi -f
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
