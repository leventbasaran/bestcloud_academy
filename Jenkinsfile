pipeline {
  agent {
    docker {
      image 'garyear/bcfmacdemy:latest'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'docker run --env webhook_url -p 5000:5000 --name bcfm -d garyear/bcfmacdemy:latest'
      
      }
    }
  }
}
