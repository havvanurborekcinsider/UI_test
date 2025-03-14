pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                // Git reposunu çek
                git(
                    branch: 'main', 
                    url: 'git@github.com:havvanurborekcinsider/UI_test.git', 
                    credentialsId: 'git_key'
                )
            }
        }

        stage('Install Dependencies') {
            steps {
                // npm yükleme yolunu belirterek bağımlılıkları yükle
                sh '/opt/homebrew/bin/npm install'
            }
        }

        stage('Run Tests') {
            steps {
                // npm test komutunu belirli yoldan çalıştır
                sh '/opt/homebrew/bin/npm test'
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Allure raporunu oluştur
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
