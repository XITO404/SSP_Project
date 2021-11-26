# app.py는 서버를 돌리는 파일
from flask import Flask, render_template,request
import pymysql

# db 접속하는 코드
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000',db='ssp', charset='utf8')
cursor = db.cursor()

app = Flask(__name__)

# 템플릿 랜더링은 아래 구조로 사용
# @app.route('경로')
# def 파일명():
#   return render_template('파일명.확장자')
@app.route('/')
def mainpage():
    return render_template("mainpage.html")

#@app.route()
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=True)