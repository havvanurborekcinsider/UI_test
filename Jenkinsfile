pipeline {
    agent none  // Agent kullanmıyoruz, sadece main node

    environment {
        PATH = "/opt/homebrew/bin:$PATH"
        JAVA_OPTS = "-Dorg.jenkinsci.plugins.durabletask.BourneShellScript.HEARTBEAT_CHECK_INTERVAL=86400"
    }

    stages {
        stage('Workspace Cleanup') {
            agent { label 'main' }  // Main node üzerinde çalışacak
            steps {
                echo 'Workspace cleanup skipped'  // Bu adım artık atlanacak
            }
        }

        stage('Checkout') {
            agent { label 'main' }  // Main node üzerinde çalışacak
            steps {
                git(
                    branch: 'main', 
                    url: 'git@github.com:havvanurborekcinsider/UI_test.git', 
                    credentialsId: 'git_key' // Burada doğru ID olduğundan emin olun!
                )
            }
        }

        stage('Install Python & Dependencies') {
            agent { label 'main' }  // Main node üzerinde çalışacak
            steps {
                sh '''
                set -e
                brew list python || brew install python
                pip3 install -r requirements.txt || echo "Gerekli paketler zaten yüklü"
                '''
            }
        }

        stage('Install npm Dependencies') {
            agent { label 'main' }  // Main node üzerinde çalışacak
            steps {
                sh '''
                set -e
                npm install
                '''
            }
        }

        stage('Install ChromeDriver') {
            agent { label 'main' }  // Main node üzerinde çalışacak
            steps {
                sh '''
                set -e
                brew list chromedriver || brew install chromedriver
                '''
            }
        }

        stage('Run Tests') {
            agent { label 'main' }  // Main node üzerinde çalışacak
            steps {
                sh '''
                set -e
                npm test
                '''
            }
        }

        stage('Generate Allure Report') {
            agent { label 'main' }  // Main node üzerinde çalışacak
            steps {
                sh '''
                set -e
                mkdir -p allure-results
                allure generate allure-results --clean
                '''
            }
        }

        stage('Publish Allure Report') {
            agent { label 'main' }  // Main node üzerinde çalışacak
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
