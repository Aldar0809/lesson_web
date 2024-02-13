from flask import Flask, render_template

app = Flask(__name__)

@app.route('/list_prof/<string:list_type>')
def list_prof(list_type):
    professions = ["Engineer", "Doctor", "Astronaut", "Scientist", "Geologist"]
    if list_type == 'ol':
        return render_template('list.html', professions=professions, list_type='ol')
    elif list_type == 'ul':
        return render_template('list.html', professions=professions, list_type='ul')
    else:
        return "Invalid parameter. Please use 'ol' for ordered list or 'ul' for unordered list."

if __name__ == "__main__":
    app.run(port=8000, host='147.45.77.43')
