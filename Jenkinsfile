pipeline {
    agent any
    environment {
        GIT_SSH_COMMAND = 'ssh -o StrictHostKeyChecking=no' // SSH anahtarı kontrolünü devre dışı bırakıyoruz
    }

    stages {
        stage('Checkout') {
            steps {
                // Git reposunu SSH ile çekmek için
                git(
                    branch: 'main', 
                    url: 'git@github.com:havvanurborekcinsider/UI_test.git', 
                    credentialsId: 'git_key' // SSH anahtar kimlik bilgisi
                )
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Bağımlılıkları yükle
                    sh '''#!/bin/bash
                    npm install
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Testleri çalıştır
                    sh '''#!/bin/bash
                    npm test
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Allure raporu oluştur
                    sh '''#!/bin/bash
                    allure generate allure-results --clean
                    '''
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                script {
                    // Allure raporunu yayımla
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                }
            }
        }
    }

    post {
        always {
            // Pipeline sonrası her durumda bu adımlar çalışır
            echo 'Pipeline completed'
        }
    }
}
