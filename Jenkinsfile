pipeline {
  agent any
  stages {
    stage('Build Container') {
      steps {
        bat "docker build -t aman1 ."
      }
    }
    stage('run_container'){
         steps{
           bat "docker run -d aman -p 5001:5000 aman1"
         }
    }
  }
}
