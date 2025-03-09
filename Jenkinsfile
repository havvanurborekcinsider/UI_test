pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/havvanurborekcinsider/UI_test.git'  // Repo URL'si
    }

    stages {
        stage('Checkout') {
            steps {
                // GitHub reposunu checkout edin
                git branch: 'main', url: "$REPO_URL"
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Gereksinimleri yükleyin (örneğin Node.js, Python veya başka bir framework)
                    sh 'npm install'  // Eğer Node.js ile çalışıyorsanız
                    // veya
                    // sh 'pip install -r requirements.txt'  // Eğer Python ile çalışıyorsanız
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // UI testlerini çalıştırın
                    sh 'pytest --maxfail=1 --disable-warnings -q'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Allure raporunu oluşturun
                    sh 'allure generate allure-results --clean -o allure-report'
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-report']]
            }
        }
    }

    post {
        always {
            // Testlerin ardından raporları ve ekran görüntülerini saklayın
            archiveArtifacts allowEmptyArchive: true, artifacts: '**/allure-report/**'
        }
    }
}
