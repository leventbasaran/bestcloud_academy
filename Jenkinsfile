pipeline {
	agent any
	    stages {
	        stage('Clone Repository') {
	        /* Cloning the repository to our workspace */
	        steps {
	        checkout scm
	        }
	   }
	   stage('Build Image') {
	        steps {
		  docker {
     	 image 'garyear/bcfmacdemy:latest'
    }
	   }
	   stage('Run Image') {
	        steps {
	        sh 'docker run --env webhook_url -d -p 5000:5000 --name bcfmv3 garyear/bcfmacdemy'
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}
