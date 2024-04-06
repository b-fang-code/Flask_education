# Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет
# отображаться форма для загрузки изображений.


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Главная страница с изображением и ссылкой на загрузку
@app.route('/')
def index():
    return render_template('index.html')


# Страница загрузки изображения
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Обработка загруженного изображения
        image = request.files['image']
        # Сохраните изображение в нужной директории
        # Например, сохраните его как my_image.jpg
        image.save('static/my_image.jpg')
        return redirect(url_for('index'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
