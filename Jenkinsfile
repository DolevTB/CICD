pipeline {
    agent any

    stages {
        stage('Run ansible') {
            steps {
                sh 'ansible-playbook -i Ansible/aws_ec2.yml Ansible/infra.yml'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "bye"
            }
        }
    }
}