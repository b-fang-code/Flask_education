# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/<int:a>/<int:b>')
def sum_num(a, b):
    return str(a + b)


@app.route('/<string:text>/')
def len_tex(text):
    return str(len(text))


if __name__ == '__main__':
    app.run()
