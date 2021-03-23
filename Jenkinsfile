pipeline {
  agent {
    docker {
      image 'garyear/bcfmacdemy:latest'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'docker run --env webhook_url -p 5000:5000 --name bcfm -d levent'
      
      }
    }
  }
  environment {
    webook_url = 'https://webhook.site/52a618cb-0f1e-4ac7-8b16-4b64b295f932'
  }
}
