pipeline {
    agent {
        docker { image 'python:latest' }
    }

    stages {
        stage('Pre-build') {
            steps {
                sh "pip install poetry"
                sh "poetry install"
            }
        }
        stage('Test') {
            parallel {
                stage('UnitTests') {
                    steps {
                        sh "poetry run python -m unittest discover tests -p \"test_*.py\""
                    }
                }
                stage('TypeChecking') {
                    steps {
                        sh "poetry run mypy gmconfig"
                    }
                }
                stage('Linting') {
                    steps {
                        sh "poetry run black --check"
                    }
                }
            }

        }
        stage('Release') {
            when {
                branch 'master'
            }
            environment {
                PYPI_CREDS = credentials('pypi')
            }
            steps {
                sh "poetry publish --build --username $PYPI_CREDS_USR --password $PYPI_CREDS_PSW"
            }
        }
    }
}