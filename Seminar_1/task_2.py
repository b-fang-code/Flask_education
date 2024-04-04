# Добавьте две дополнительные страницы в ваше веб-приложение: страницу "about" и страницу "contact".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


if __name__ == '__main__':
    app.run(debug=True)
