# Создать базу данных для хранения информации о студентах университета. База данных должна содержать две таблицы:
# "Студенты" и "Факультеты". В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа
# и id факультета. В таблице "Факультеты" должны быть следующие поля: id и название факультета. Необходимо создать
# связь между таблицами "Студенты" и "Факультеты". Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.


from flask import Flask, render_template
from faker import Faker
from models_01 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)
fake = Faker()


@app.route('/')
def index():
    return "Hello"


@app.cli.command('create')
def initdb():
    db.create_all()


@app.cli.command('initdb')
def initdb_command():
    faculties = []  # Создаем пустой список для хранения объектов faculty
    for fac in range(4):
        faculty = Faculty(name=fake.job())
        db.session.add(faculty)
        faculties.append(faculty)  # Добавляем созданный объект faculty в список
    db.session.commit()

    for i in range(12):
        student = Student(
            name=fake.first_name(),
            last_name=fake.last_name(),
            age=fake.random_int(min=18, max=30),
            gender=fake.random_element(elements=("male", "female")),
            group=fake.random_int(min=1, max=10),
            faculty_id=fake.random_element(elements=faculties).id
        )
        db.session.add(student)
    db.session.commit()


@app.route('/students')
def get_students():
    students = Student.query.all()
    faculties = Faculty.query.all()
    context = {
        'students': students,
        'faculties': faculties,
    }
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
