pipeline {
    agent {
        docker { image 'python:3.7-alpine' }
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
                        sh "poetry run black --check gmconfig"
                    }
                }
            }

        }
        stage('Build') {
            steps {
                sh "poetry build"
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
                sh "poetry publish --username $PYPI_CREDS_USR --password $PYPI_CREDS_PSW"
            }
        }
    }
}