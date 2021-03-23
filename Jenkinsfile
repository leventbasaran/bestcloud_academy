pipeline {
  agent { docker { image 'python:3.7.2-stretch' } }
  stages {
    stage('build') {
      steps {
        sh 'docker build -t levent .'
      }
    }
    stage('test') {
      steps {
        sh 'docker run --env webhook_url -p 5000:5000 --name bcfm -d levent'
      }   
    }
  }
}
