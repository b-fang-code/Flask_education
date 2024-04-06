# Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на которую будет переход на другую страницу
# с приветствием пользователя по имени.


from flask import Flask, render_template, request

app = Flask(__name__)


# Главная страница с кнопкой
@app.route('/')
def index():
    return render_template('index.html')


# Страница приветствия с именем пользователя
@app.route('/greeting/', methods=['POST'])
def greeting():
    user_name = request.form.get('user_name')
    return render_template('greeting.html', user_name=user_name)


if __name__ == '__main__':
    app.run(debug=True)
