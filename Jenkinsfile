pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Git reposunu çek
                git 'git@github.com:havvanurborekcinsider/UI_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Bağımlılıkları yükle
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                // Testleri çalıştır
                sh 'npm test'
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Allure raporu oluştur
                sh 'allure generate allure-results --clean'
            }
        }

        stage('Publish Allure Report') {
            steps {
                // Allure raporunu yayımla
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            // Pipeline sonrası mesaj
            echo 'Pipeline completed'
        }
    }
}
