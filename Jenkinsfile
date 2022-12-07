pipeline {
  agent any
  stages{    
    stage('Build Container') {
      steps {
        sh "docker build -t aman1 ."
      }
    }
    stage('run_container'){
         steps{
           sh "docker run -d --name aman -p 5001:5000 aman1"
         }
    }
  }
}
