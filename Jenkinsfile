pipeline {
    agent any
   

    environment {
       GITNAME = 'oolralra'
       GITEMAIL = 'oolralra@gmail.com'
       GITWEBADD = 'https://github.com/oolralra/fast-code.git' // 소스코드 업로드된 깃허브
       GITDEPADD = 'git@github.com:oolralra/fast-deployment.git' // 매니페스트 파일이 있는 깃레포 주소
        // 환경변수 정의 가능.
       GITCREDENTIAL = 'git_cre' // 빌드프로젝트 생성시 만들어놓은 git_cre
       DOCKERHUB = 'oolralra/fast-image' // 컨테이너 이미지를 push할 이미지 레지스트리
       DOCKERHUBCREDENTIAL = 'docker_cre' // 해당 레지스트리에 로그인 정보, 도커허브의 ID/PASS
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
        
        stage('code build') {
        // 빌드 단계
            steps {
                echo 'build command'

               
            }
       
            post {
            // 상단 steps의 성공 혹은 실패에 따라 수행할 동작 정의
                failure {
                    echo 'build failure'
                }
                success {
                    echo 'build success'
                }
            }
        }
        
        stage('image build') {
        // 이미지 빌드
            steps {
                sh "docker build -t ${DOCKERHUB}:${currentBuild.number} ./main"
                sh "docker build -t ${DOCKERHUB}:latest ./main"
                // currentBuild.number = 젠킨스가 제공하는 빌드넘버 변수
                // oolralra/fast-image:1 같은 형태로 이미지가 만들어 질 것.
            }
       
            post {
            // 상단 steps의 성공 혹은 실패에 따라 수행할 동작 정의
                failure {
                    echo 'image build failure'
                }
                success {
                    echo 'image build success'
                }
            }
        }
        
        stage('image push') {
        // 이미지 push
            steps {
                
                withDockerRegistry(credentialsId: DOCKERHUBCREDENTIAL, url: '') {
                    sh "docker push ${DOCKERHUB}:${currentBuild.number}"
                    sh "docker push ${DOCKERHUB}:latest"
                }
            }
       
            post {
            // 상단 steps의 성공 혹은 실패에 따라 수행할 동작 정의
                failure {
                    echo 'image push failure'
                }
                success {
                    echo 'image push success'
                }
            }
        }
        
        stage('k8s manifest file update') {
            steps {
                
                
                git credentialsId: GITCREDENTIAL,
                url: GITDEPADD,
                branch: 'main'
        
                // 이미지 태그 변경 후 메인 브랜치에 푸시
                sh "git config --global user.email ${GITEMAIL}"
                sh "git config --global user.name ${GITNAME}"
                sh "sed -i 's@${DOCKERHUB}:.*@${DOCKERHUB}:${currentBuild.number}@g' deployment.yml"
        
                sh "git add ."
                sh "git commit -m 'fix:${DOCKERHUB} ${currentBuild.number} image versioning'"
                sh "git branch -M main"
                sh "git remote remove origin"
                sh "git remote add origin ${GITDEPADD}"
                sh "git push -u origin main"

            }
            post {
                failure {
                echo 'k8s manifest file update failure'
                }
                success {
                slackSend (channel: '#dep02', color: '#FFFF00', message:
                "MANIFEST UPDATE SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
                
                echo 'k8s manifest file update success'
                // ㅇㅇㅇ
                }
            }
        }

    }
}
