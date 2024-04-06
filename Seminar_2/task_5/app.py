# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить", при нажатии на которую будет произведено вычисление
# результата выбранной операции и переход на страницу с результатом.


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def request_():
    return render_template('request.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['first'])
    b = float(request.form['second'])
    operation = request.form['operation']
    match operation:
        case 'plus':
            result = a + b
        case 'minus':
            result = a - b
        case 'mult':
            result = a * b
        case 'div':
            if b == 0:
                result = 'inf'
            else:
                result = a / b
        case _:
            result = None
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
