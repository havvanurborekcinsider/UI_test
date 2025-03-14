pipeline {
    agent any

    environment {
        // OpenJDK 17 için JAVA_HOME ve PATH ayarları
        JAVA_HOME = '/opt/homebrew/opt/openjdk@17'
        PATH = "${JAVA_HOME}/bin:/opt/homebrew/bin:$PATH"  // JAVA_HOME'u PATH'e ekliyoruz
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
                    credentialsId: 'github_key'
                )
            }
        }

        stage('Check File Paths and Permissions') {
            steps {
                script {
                    // Geçerli dizini kontrol et ve dosya listesi yazdır
                    sh '''
                    echo "Current directory: $(pwd)"  # Geçerli dizini yazdırır
                    echo "Listing files in current directory"
                    ls -l  # Geçerli dizindeki dosyaları listeler
                    '''
                }
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                sh '''
                set -e
                if ! brew list python; then
                    brew install python
                fi
                # Python bağımlılıklarını yükle (örneğin pytest)
                pip install -r requirements.txt
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

        stage('Install Allure') {
            steps {
                sh '''
                set -e
                if ! brew list allure; then
                    brew install allure
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                set -e
                python3 lcw_test.py  # Python testini çalıştır
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                set -e
                mkdir -p allure-results
                # Allure raporunu oluştur
                allure generate allure-results --clean -o allure-report
                '''
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
            echo 'Pipeline completed'
        }
    }
}
