pipeline {
    agent any

    stages {
        stage('Limpiar contenedor e imagen') {
            steps {
                sh '''
                    docker stop fastapi-dolarapi || true
                    docker rm fastapi-dolarapi || true
                    docker rmi fastapi-dolarapi || true
                '''
            }
        }

        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/okee-arch/Evaluacion-N2-DRY7122.git'
            }
        }

        stage('Construir imagen') {
            steps {
                sh 'docker build -t fastapi-dolarapi .'
            }
        }

        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run -d --name fastapi-dolarapi -p 8000:8000 fastapi-dolarapi'
            }
        }
    }
}
