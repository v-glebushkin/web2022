from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(
    host="localhost",
    database="web",
    user="postgres",
    password="071778Ckfdf%"
)
cursor = conn.cursor()

success_message = {'success': True}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/', methods=['GET'])
def get_users():
    user_data = []
    sql = 'SELECT * FROM main;'
    cursor.execute(sql)
    data = cursor.fetchall()
    for user in data:
        user_data.append({'id': user[0], 'name': user[1], 'surname': user[2], 'phone number': user[3]})
    return render_template('users.html', users=user_data)


@app.route('/users/<int:userid>', methods=['GET'])
def get_user(userid):
    userid_data = []
    sql = 'SELECT * FROM main WHERE id = %s'
    cursor.execute(sql, (int(userid),) )
    data = cursor.fetchall()
    for userid in data:
        userid_data.append({'id': userid[0], 'name': userid[1], 'surname': userid[2], 'phone number': userid[3]})
    return render_template('user.html', users=userid_data)


@app.route('/users/', methods=['POST'])
def add_user():
    sql = 'INSERT INTO main VALUES (%s, %s, %s, %s);'
    id = request.json['id']
    name = request.json['name']
    surname = request.json['surname']
    tel = request.json['tel']
    cursor.execute(sql, (id, name, surname, tel))
    conn.commit()
    return get_users()


@app.route('/users/<int:userid>', methods=['DELETE'])
def del_user(userid):
    sql = 'DELETE FROM main WHERE id = %s'
    cursor.execute(sql, (int(userid),))
    conn.commit()
    return get_users()


@app.route('/users/<int:userid>', methods=['PUT'])
def update_user(userid):
    sql = 'UPDATE main SET name = %s, surname = %s, tel = %s WHERE id = %s'
    name = request.json['name']
    surname = request.json['surname']
    tel = request.json['tel']
    cursor.execute(sql, (name, surname, tel, int(userid)))
    conn.commit()
    return get_user(userid)


if __name__ == '__main__':
    app.run(debug=True)