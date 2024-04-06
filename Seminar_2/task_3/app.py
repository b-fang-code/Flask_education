# Создать страницу, на которой будет форма для ввода логина и пароля, при нажатии на кнопку "Отправить"
# будет произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя
# или страницу с ошибкой.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Главная страница с формой входа
@app.route('/')
def login():
    return render_template('login.html')


# Проверка логина и пароля
@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Здесь вы можете добавить логику проверки логина и пароля
    # Например, сравнить с предопределенными значениями

    if username == 'admin' and password == 'secret':
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('error'))


# Страница приветствия
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# Страница с ошибкой
@app.route('/error')
def error():
    return "<h1>Ошибка! Неверный логин или пароль.</h1>"


if __name__ == '__main__':
    app.run(debug=True)
