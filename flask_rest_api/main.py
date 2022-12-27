import json
from flask import Flask, jsonify, request
import psycopg2
app = Flask(__name__)
data = [{'name': 'Alex', 'surname': 'Turner'}]


conn = psycopg2.connect(
    host="localhost",
    database="start",
    user="postgres",
    password="071778Ckfdf%"
)
cursor = conn.cursor()

success_message = {'success': True}


@app.route('/users', methods=['GET'])
def get_users():
    sql = 'SELECT * FROM t1_main;'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return jsonify(data)


@app.route('/users', methods=['POST'])
def add_user():
    return jsonify(data)


@app.route('/users', methods=['DELETE'])
def del_user():
    return jsonify(data)


# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify(data)
#
#
# @app.route('/users', methods=['POST'])
# def add_user():
#     print(request.get_json()['name'])
#     data.append({'name': 'Matt'})
#     return jsonify(data)
#
#
# @app.route('/users', methods=['DELETE'])
# def del_user():
#     return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)