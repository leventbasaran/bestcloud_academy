pipeline {
  stages {
 stage (' Image Building') {
         docker.build("garyear/bcfmacdemy:latest")
    }
  }
    stage('test') {
      steps {
        sh " docker run --env webhook_url -p 5000:5000 --name bcfm -d garyear/bcfmacdemy:latest"
        echo 'test'
      
      
     }
   }
 }

