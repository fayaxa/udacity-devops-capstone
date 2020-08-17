pipeline{
    environment{
        dockerHub = 'fayax'
        dockerImage = 'devops-capstone-app'
    }
    agent{}
    stages{
        stage('Linting'){
            step{
                sh 'hadolint Dockerfile'
                sh 'pylint --disable=R,C,W1203 app.py'
            }
        }
        stage('Build Docker Image'){
            step{
                sh 'docker build --tag=devops-capstone-app .'
            }
        }
        stage('Push Docker Image'){
            step{
                withDockerRegistery([url: "", credentialsId: "dockerhub"]){
                    sh 'docker image tag devops-capstone-app fayax/devops-capstone-app'
                    sh 'docker push fayax/devops-capstone-app'
                }
            }
        }
        stage('Deploy'){
            step{
                withAWS(credentials: 'aws-static', region: 'us-west-2'){
                    sh "aws eks --region us-west-2 update-kubeconfig --name devopscapstonecluster"
                    sh "kubectl config use-context arn:aws:eks:us-west-2:923635882480:cluster/devopscapstonecluster"
                    sh 'kubectl apply -f deployment.yml'
                    sh "kubectl get nodes"
                    sh "kubectl get deployment"
                    sh "kubectl get pod -o wide"
                    sh "kubectl get service/devops-capstone-app"
                }

            }
        }
        stage('Clean Up'){
            step{
                sh 'docker system prune'
            }
        }
    }
    post{
        success{
            echo 'Jenkins pipeline completed successfully!'
        }
        failure{
            echo 'Jenkins pipeline failed!'
        }
    }
}
        post{
            success{
                echo 'Jenkins pipeline completed successfully!'
            }
            failure{
                echo 'Jenkins pipeline failed!'
            }
        }
}
