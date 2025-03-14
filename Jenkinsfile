pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:$PATH"
    }

    stages {
        stage('Workspace Cleanup') {
            steps {
                deleteDir()  // Çalışma alanını temizle
            }
        }

        stage('Checkout') {
            steps {
                git(
                    branch: 'main', 
                    url: 'git@github.com:havvanurborekcinsider/UI_test.git', 
                    credentialsId: 'git_key'
                )
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                sh 'brew install python || echo "Python zaten yüklü"'
                sh 'pip3 install selenium || echo "Selenium zaten yüklü"'
            }
        }

        stage('Install npm Dependencies') {
            steps {
                sh '/bin/bash -c "/opt/homebrew/bin/npm install"'
            }
        }

        stage('Install ChromeDriver') {
            steps {
                sh 'brew install chromedriver || echo "ChromeDriver zaten yüklü"'
            }
        }

        stage('Run Tests') {
            steps {
                sh '/bin/bash -c "npm test"'
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '/bin/bash -c "allure generate allure-results --clean"'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
    }
}
