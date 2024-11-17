pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-app"  // Replace with your app name
        DOCKER_REGISTRY = "volkravchuk"  // Replace with your container registry username
        KUBE_DEPLOYMENT_NAME = "my-flask-app"
        KUBE_NAMESPACE = "default"  // Replace with your Kubernetes namespace
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker image to registry...'
                withDockerRegistry([credentialsId: 'docker-registry-credentials', url: 'https://index.docker.io/v1/']) {
                    sh '''
                        docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying application to Kubernetes...'
                sh '''
                    kubectl apply -f - <<EOF
                    apiVersion: apps/v1
                    kind: Deployment
                    metadata:
                      name: ${KUBE_DEPLOYMENT_NAME}
                      namespace: ${KUBE_NAMESPACE}
                    spec:
                      replicas: 2
                      selector:
                        matchLabels:
                          app: ${KUBE_DEPLOYMENT_NAME}
                      template:
                        metadata:
                          labels:
                            app: ${KUBE_DEPLOYMENT_NAME}
                        spec:
                          containers:
                          - name: ${KUBE_DEPLOYMENT_NAME}
                            image: ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest
                            ports:
                            - containerPort: 5000
                    EOF
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
