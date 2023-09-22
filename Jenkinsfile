pipeline {
  agent any

  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Ujstor/streamlit-working-hours/', branch: 'master')
      }
    }

    stage('Test') {
      steps {
        script {
          sh "${JENKINS_HOME}/scripts/pytest.sh ${WORKSPACE}"
        }
      }
    }

    stage('Build') {
      steps {
        script {
          sh 'docker build -t ujstor/working_hours .'
        }
      }
    }

    stage('Deploy') {
      steps {
        script {
          sh 'docker push ujstor/working_hours'
        }
      }
    }
  }
}