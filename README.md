# script2sami.py
 - Script.xml 파일을 SAMI 자막으로 변환하는 프로그램
   - 직접 실행하거나, smiserver 를 통해서 실행가능
 - mkSami 함수는 최종 결과 문자열을 반환하는 함수
   - 입력 파일 경로를 받아서 처리 가능
   - 입력 파일 object 를 받아서 처리 가능
 - main 함수는 mkSami 의 결과를 stdout 에 출력

## 실행방법

python script2sami.py myscript.xml

# smiserver
 - script2sami.py 기능을 웹으로 서비스 하도록 flask 를 붙임

## 실행방법

FLASK_APP=smiserver.py flask run --host=0.0.0.0
