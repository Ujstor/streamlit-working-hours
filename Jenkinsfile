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

  }
}