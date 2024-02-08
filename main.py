from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<prof>')
@app.route('/training/<prof>')
def index(prof):
    return render_template('base.html', job=prof)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
