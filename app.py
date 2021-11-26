# app.py는 서버를 돌리는 파일
from flask import Flask, render_template,request,session
import pymysql

app = Flask(__name__)

# db 접속하는 코드
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000',db='ssp', charset='utf8')
cursor = db.cursor()


# 템플릿 랜더링은 아래 구조로 사용
# @app.route('경로')
# def 파일명():
#   return render_template('파일명.확장자')

@app.route('/')
def mainpage():
    return render_template("mainpage.html")

@app.route('/calender.html')
def calender():
    return render_template("./templates/calender.html")

@app.route('/todo.html')
def todo():
    return render_template("todo.html")

@app.route('/login.html')
def login():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        try:
            if (id in Member):

                session["logged_in"] = True
                return render_template('login.html')
            else:
                return '비밀번호가 틀립니다.'
            return '아이디가 없습니다.'
        except:
            return 'Dont login'
    else:
        return render_template('./templates/login.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # 응답을 받았으면:
        name = request.form['name']
        email = request.form['email']
        id = request.form['id']
        pw = request.form['pw']

        sql = '''INSERT INTO Member (name,email,id,pw) VALUES (%s, %s, %s,%s);'''

        cursor.execute(sql, (name, email, id, pw))
        db.commit()

        # return redirect(request.url)
        return render_template('login.html')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)