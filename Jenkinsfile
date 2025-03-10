pipeline {
    agent any

    environment {
        // PATH çevresel değişkeni, gerekli araçların bulunduğu dizini ekliyoruz
        PATH = "/opt/homebrew/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                // Git reposunu çekmek için
                git branch: 'main', url: 'https://github.com/havvanurborekcinsider/UI_test.git'
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
                    allure generate --clean
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
