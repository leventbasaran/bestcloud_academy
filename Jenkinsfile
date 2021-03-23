pipeline {
  agent { docker }
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
