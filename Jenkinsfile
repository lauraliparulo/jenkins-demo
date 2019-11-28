node('master') {

    stage('Testing') {

    
      step {
             printMessage('run test pipeline')
          sh 'python test_sum.py'
                 sh 'cd test'
               sh 'python subtraction-tests.py'
                   printMessage('Tests completed')
             }
   
             
    
        
    }
}

def printMessage(message){
     echo "${message}"
}
