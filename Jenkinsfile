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
	        sh 'sudo docker build -t bcfm:v3 .'
	        }
	   }
	   stage('Run Image') {
	        steps {
	        sh 'sudo docker run --env webhook_url -d -p 5000:5000 --name bcfmv3 bcfm:v3'
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}
