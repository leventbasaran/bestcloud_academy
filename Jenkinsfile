pipeline {
	agent any
	
	environment {
        webhook_url = "https://webhook.site/52a618cb-0f1e-4ac7-8b16-4b64b295f932"
	}
	    stages {
	   stage('Pull Image') {
	        steps {
	        sh 'docker image -t bcfm .'
	        }
	   }
	   stage("Env Variables") {
            steps {
                sh "printenv"
            }
	   }    
	   stage('Run Image') {
	        steps {
	        sh 'docker run --env webhook_url -p 5000:5000 -d bcfm'

	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Oluşturma başarılı.'
	            }
	   }
    }
}
