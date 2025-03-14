pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:$PATH"
        JAVA_OPTS = "-Dorg.jenkinsci.plugins.durabletask.BourneShellScript.HEARTBEAT_CHECK_INTERVAL=86400"
    }

    stages {
        stage('Workspace Cleanup') {
            steps {
                echo 'Workspace cleanup skipped'
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
                sh '''
                set -e
                if ! brew list python; then
                    brew install python
                fi
                if ! pip3 show -q -f requirements.txt; then
                    pip3 install -r requirements.txt || echo "Gerekli paketler zaten yüklü"
                fi
                '''
            }
        }

        stage('Install npm Dependencies') {
            steps {
                sh '''
                set -e
                if ! npm list -g; then
                    npm install
                fi
                '''
            }
        }

        stage('Install ChromeDriver') {
            steps {
                sh '''
                set -e
                if ! brew list chromedriver; then
                    brew install chromedriver
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                set -e
                npm test
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                set -e
                mkdir -p allure-results
                allure generate allure-results --clean
                '''
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
