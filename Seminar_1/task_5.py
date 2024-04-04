# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".


from flask import Flask

app = Flask(__name__)

html_ = """<h1>Моя первая html страница</h1><br><p>Привет, мир!</p>"""


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/page/')
def page():
    return html_


if __name__ == '__main__':
    app.run()
