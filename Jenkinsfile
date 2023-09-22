pipeline {
  agent any
  stages {
    stage('Checkput code') {
      parallel {
        stage('Checkput code') {
          steps {
            git(url: 'https://github.com/Ujstor/streamlit-working-hours/', branch: 'master')
          }
        }

        stage('Checkout code') {
          steps {
            git(branch: 'tests', url: 'https://github.com/Ujstor/streamlit-working-hours')
          }
        }

      }
    }

    stage('Test') {
      steps {
        sh '${JENKINS_HOME}/scripts/pytest.sh ${WORKSPACE}'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t ujstor/working_hours .'
      }
    }

    stage('Deploy') {
      steps {
        sh '''

  docker push ujstor/working_hours'''
      }
    }

  }
}