node('master') {

    stage('Testing') {
                sh 'python test_sum.py'
            }
    
    dir('test') {
         printMessage('run pipeline')
        stage('Testing') {
                sh 'python subtraction-tests.py'
            }
             
             printMessage('Tests completed')
        
    }
}

def printMessage(message){
     echo "${message}"
}
