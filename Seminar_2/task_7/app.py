# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить", при нажатии на которую будет
# перенаправление на страницу с flash сообщением, где будет выведено "Привет, [имя]!".
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Установите секретный ключ для flash сообщений


@app.route('/', methods=['GET', 'POST'])
def flash_message():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flash_message'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
