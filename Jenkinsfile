node('master') {

    stage('Testing') {
   printMessage('run test pipeline')
    
      steps {
          sh 'python test_sum.py'
                 sh 'cd test'
               sh 'python subtraction-tests.py'
             }
   
             
             printMessage('Tests completed')
        
    }
}

def printMessage(message){
     echo "${message}"
}
