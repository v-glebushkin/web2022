from flask import Flask
from flask import request, make_response, redirect, abort, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # response = make_response('<h1>Set cookie</h1>')
    # response.set_cookie('answer', '42')
    # return response
    user_list = ['Ivan', 'Alex', 'Dima']
    return render_template('index.html', users=user_list)

@app.route('/ya')
def ya():
    return redirect('https://ya.ru')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# @app.route('/user/<name>')
# def user(name):
#     user_agent = request.headers.get('User-Agent')
#     if name != 'Slava':
#         abort(404)
#     return '<h1>Hello {}!</h1><br>Your User-Agent is {}'.format(name, user_agent)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug = True)