# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить",
# при нажатии на которую будет произведена проверка возраста и переход на страницу с результатом или на страницу
# с ошибкой в случае некорректного возраста.


from flask import Flask, render_template, request

app = Flask(__name__)

MAX_AGE = 18


@app.route('/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        name = request.form.get('name')
        if age < MAX_AGE:
            return render_template('error.html')
        else:
            return render_template('result.html', name=name, age=age)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
