node('master') {

    dir('test') {
         printMessage('run pipeline')
        stage('Testing') {
                sh 'python test/subtraction-tests.py'
            }
             
             printMessage('Tests completed')
        
    }
}

def printMessage(message){
     echo "${message}"
}
