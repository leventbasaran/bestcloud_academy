pipeline {
   stage('Get Source') {
      // copy source code from local file system and test
      // for a Dockerfile to build the Docker image
      git ('https://github.com/leventbasaran/bestcloud_academy.git')
      if (!fileExists("Dockerfile")) {
         error('Dockerfile missing.')
      }
   }
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
         sh "docker build -t bcfm:v4 ."
   }
   stage("run docker container"){
        sh "sudo docker run --env webhook_url -p 5000:5000 --name bcfmv4 -d bcfm:v4 "
    }
}
