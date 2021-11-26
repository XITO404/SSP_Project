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
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)


@app.route('/signup.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form['name']
        email=request.form['email']
        id=request.form['id']
        pw = request.form['pw']

        sql = "INSERT INTO Member (name,email,id,pw) VALUES (%s, %s, %s,%s);" %(name,email,id,pw)

        cursor.execute(sql, (name, email,id,pw))
        db.commit()

        # return redirect(request.url)
        return render_template('login.html')

    return render_template('login.html')