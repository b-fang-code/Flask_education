# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл". Данные о студентах должны
# быть переданы в шаблон через контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/users/')
def user_():
    dict_ = [
        {
            'name': 'Pavel',
            'lastname': 'Vasiliev',
            'age': 36,
            'score': 4.9
        },
        {
            'name': 'John',
            'lastname': 'Smith',
            'age': 44,
            'score': 4.4
        },
        {
            'name': 'Fatush',
            'lastname': 'Gale',
            'age': 34,
            'score': 3.3
        },
    ]
    context = {
        'person': dict_
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
