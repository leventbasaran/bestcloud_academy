pipeline {
  agent {
    docker {
      image 'rbekker87/build-tools:latest'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'echo deneme'
      
      }
    }
  }
  environment {
    webook_url = 'https://webhook.site/52a618cb-0f1e-4ac7-8b16-4b64b295f932'
  }
}
