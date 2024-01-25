pipeline {
    agent any
   
    tools {
        // jenkins관리에서 maven같은 빌드툴을 정의해놓고 불러올 수 있다.
    }
    environment {
       GITWEBADD = 'https://github.com/oolralra/fast-code.git'
        // 환경변수 정의 가능.
       GITCREDENTIAL = 'git_cre'
    }
       
    stages {
        stage('Checkout Github') {
        // 깃허브 레포를 젠킨스로 다운로드.
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [],
                userRemoteConfigs: [[credentialsId: GITCREDENTIAL, url: GITWEBADD]]])

               
            }
       
            post {
            // 상단 steps의 성공 혹은 실패에 따라 수행할 동작 정의
                failure {
                    echo 'Repository clone failure'
                }
                success {
                    echo 'Repository clone success'
                }
            }
        }
        

    }
}
