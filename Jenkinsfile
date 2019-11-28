node('master') {

    dir('test') {
        stage('Testing') {
            steps {
                sh 'python test_subtraction.py'
            }
             
             printMessage('Tests completed')
        }
    }
}

def printMessage(message){
     echo "${message}"
}
