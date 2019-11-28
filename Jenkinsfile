node('master') {

    dir('test') {
        stage('Testing') {
            steps {
                sh 'python subtraction-tests.py'
            }
             
             printMessage('Tests completed')
        }
    }
}

def printMessage(message){
     echo "${message}"
}
