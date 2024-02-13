from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
def answer():
    data = {
        'title': 'Ответ',
        'surname': 'Иванов',
        'name': 'Иван',
        'education': 'Высшее',
        'profession': 'Инженер',
        'sex': 'Мужской',
        'motivation': 'Хочу исследовать Марс',
        'ready': 'Да'
    }
    return render_template('auto_answer.html', **data)


@app.route('/auto_answer')
def auto_answer():
    data = {
        'title': 'Автоответ',
        'surname': 'Петров',
        'name': 'Петр',
        'education': 'Среднее',
        'profession': 'Рабочий',
        'sex': 'Мужской',
        'motivation': 'Хочу заработать деньги',
        'ready': 'Нет'
    }
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run()
