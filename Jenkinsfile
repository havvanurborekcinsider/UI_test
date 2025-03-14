pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:$PATH"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                // Workspace'i temizle
                cleanWs()
            }
        }

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

        stage('Install Python') {
            steps {
                // Python'ı yükleyin (eğer yüklenmemişse)
                sh 'brew install python'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                // Python bağımlılıklarını yükle (selenium gibi)
                sh '/opt/homebrew/bin/pip3 install selenium'
            }
        }

        stage('Install Dependencies') {
            steps {
                // npm bağımlılıklarını yükle
                sh '/bin/bash -c "/opt/homebrew/bin/npm install"'
            }
        }

        stage('Install ChromeDriver') {
            steps {
                // ChromeDriver'ı yükle (Selenium için gerekli)
                sh 'brew install chromedriver'
            }
        }

        stage('Run Tests') {
            steps {
                // Testleri çalıştır
                sh '/bin/bash -c "/opt/homebrew/bin/npm test"'
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Allure raporu oluştur
                sh '/bin/bash -c "allure generate allure-results --clean"'
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
