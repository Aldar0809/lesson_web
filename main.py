from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


@app.route('/index')
def return_index_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                  <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def return_promo_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                  <h1>Человечество вырастает из детства.</h1>
                  <h1>Человечеству мала одна планета.</h1>
                  <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                  <h1>И начнем с Марса!</h1>
                  <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route('/image_mars')
def return_image_mars_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                  <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/image.png')}" 
                  alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')

# commit image mars