# app.py는 서버를 돌리는 파일
from flask import Flask, session, render_template, redirect, request, url_for, flash, jsonify, json
# from flaskext.mysql import MySQL

import pymysql

app = Flask(__name__)
app.config["SECRET_KEY"] = "ABCD"
# db 접속하는 코드
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000',db='ssp', charset='utf8')
cursor = db.cursor()


### 초기 테이블 생성 ###
create_todos_table_query = 'CREATE TABLE todos ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, userid varchar(50) NOT NULL, todo varchar(200) NOT NULL, checked boolean not null default 0, date date NOT NULL, likes int NOT NULL default 0, dislikes int NOT NULL default 0);'
create_friends_table_query = 'CREATE TABLE friends ( following varchar(50) NOT NULL, follower varchar(50) NOT NULL, date date NOT NULL);'
try:
    cursor.execute(create_todos_table_query)
    print(">>> todo table create complete")
except Exception as e:
    print(">>> todo table already exists")

try:
    cursor.execute(create_friends_table_query)
    print(">>> friends table create complete")
except Exception as e:
    print(">>> friends table already exists")
#####################



# 템플릿 랜더링은 아래 구조로 사용
# @app.route('경로')
# def 파일명():
#   return render_template('파일명.확장자')

@app.route('/')
def main_page():
    return render_template("bootstrap_mainpage.html")

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/todo/')
def todo():
    return render_template("todo.html")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        id=request.form['id']
        pw = request.form['pw']
        # name=request.form['name']
        sql = f"select * from Member where id='{id}' and pw='{pw}'"

        # sql = f"select * from Member where id='{id}'"
        cursor.execute(sql)

        session['asd']=id

        cursor.execute(sql)
        rows = cursor.fetchall()

        if len(rows)==1:
            flash("로그인 성공")
            return redirect(url_for('main_page'))
        else:
            flash("로그인 실패")
            return render_template("login.html")
    elif request.method == 'GET':
        return render_template("login.html")

@app.route('/signup/' , methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        id = request.form['id']
        pw = request.form['pw']

        sql = f"INSERT INTO Member(name,email,id,pw) VALUES ('{name}', '{email}', '{id}', '{pw}')"

        cursor.execute(sql)
        db.commit()

        # return redirect(request.url)
        return render_template('login.html')
    elif request.method == 'GET':
        return render_template("signup.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        id = request.form['id']
        pw = request.form['pw']

        sql = f"INSERT INTO Member(name,email,id,pw) VALUES ('{name}', '{email}', '{id}', '{pw}')"

        cursor.execute(sql)
        db.commit()

        return redirect(request.url)
        return render_template('login.html')

    return render_template('login.html')



@app.route('/logout/',methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('main_page'))

@app.route('/todoinsert/',methods=['GET','POST'])
def todoinsert():
    if request.method == 'POST':
        content = request.form['content']
        date = request.form['date']
        id = session['asd']

        sql = f"insert into todos(userid, todo, checked, date, likes, dislikes) values ('{id}', '{content}', 0, '{date}', 0, 0);"

        # sql = f"INSERT INTO todo VALUES('{id}','{content}',false, '{date}')"

        cursor.execute(sql)
        db.commit()
        return redirect(request.url)
    return redirect(url_for('main_page'))

@app.route('/todoselect/',methods=['GET','POST'])
def todoselect():
    if request.method == 'POST':
        id = session['asd']
        date = request.form['date']

        sql = f"SELECT * FROM todos WHERE userid = '{id}' and DATE(date) = '{date}' "
        cursor.execute(sql)
        rows = cursor.fetchall()
        dictList = list()
        for row in rows:
            tempDict = {"content":row[1], "checked":row[2]}
            dictList.append(tempDict)
        return json.dumps(dictList)
    return redirect(url_for('main_page'))

@app.route('/tododelete/',methods=['GET','POST'])
def tododelete():
    if request.method == 'POST':
        id = session['asd']
        content = request.form['content']
        sql = f"DELETE FROM todos WHERE userid='{id}' and todo = '{content}'"
        cursor.execute(sql)
        db.commit()
        return redirect(request.url)
    return redirect(url_for('main_page'))
@app.route('/todocheck/',methods=['GET','POST'])
def todocheck():
    if request.method == 'POST':
        id = session['asd']
        content = request.form['content']
        sql = f"UPDATE todos SET checked = 1 - checked WHERE userid='{id}' and todo = '{content}'"
        cursor.execute(sql)
        db.commit()
        return redirect(request.url)
    return redirect(url_for('main_page'))

# Ranking page
@app.route('/ranking',methods=['GET'])
def rank():
    return render_template("ranking.html")

# @app.route('/login/')
# def login():
#     if request.method == 'POST':
#         id = request.form['id']
#         pw = request.form['pw']
#     return render_template('login.html')


@app.route('/calendar2/', methods=['GET', 'POST'])
def calendar2():
    return render_template("calendar2.html")


### Ajax - 팔로우 리스트 반환 ###
@app.route('/follow', methods=['get'])
def follow():
    from flask import jsonify

    id = session['asd']

    sql = f"SELECT * FROM friends WHERE follower='{id}'"

    cursor.execute(sql)
    rows = cursor.fetchall()

    follow_list = []
    for i in rows:
        follow_list.append(i[0])

    # following = rows[0]
    # data = {'following': following}

    print(f">>> follow_list : {follow_list}")

    return jsonify(follow_list)

@app.route('/search_friend/')
def search_friend():
    return render_template("search_friend.html")

if __name__ == '__main__':
    app.run(debug=True)
