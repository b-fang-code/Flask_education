# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить",
# при нажатии на которую будет произведен подсчет количества слов в тексте и переход на страницу с результатом.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('get_text.html')


@app.route('/get_text', methods=['GET', 'POST'])
def len_text():
    res = len(request.form.get('text').split())
    return render_template('result.html', result=res)


if __name__ == '__main__':
    app.run(debug=True)
