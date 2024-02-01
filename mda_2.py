import sys
from io import BytesIO
import requests
from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

toponym_to_find = ''
sps = [0.00005, 0.0005, 0.005, 0.05, 0.5, 5, 50]
now = [sps[2], 2]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_2.ui', self)
        MyWidget.initUI(self)

    def initUI(self):
        global toponym_to_find, now
        try:
            # toponym_to_find = self.line_edit.text()
            # print(toponym_to_find)
            toponym_to_find = 'Элиста'
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": toponym_to_find,
                "format": "json"}

            response = requests.get(geocoder_api_server, params=geocoder_params)

            if not response:
                # обработка ошибочной ситуации
                pass

            # Преобразуем ответ в json-объект
            json_response = response.json()
            # Получаем первый топоним из ответа геокодера.
            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]
            # Координаты центра топонима:
            toponym_coodrinates = toponym["Point"]["pos"]
            # Долгота и широта:
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

            delta = str(now[0])

            # Собираем параметры для запроса к StaticMapsAPI:
            map_params = {
                "ll": ",".join([toponym_longitude, toponym_lattitude]),
                "spn": ",".join([delta, delta]),
                "l": "map"
            }

            map_api_server = "http://static-maps.yandex.ru/1.x/"
            # ... и выполняем запрос
            response = requests.get(map_api_server, params=map_params)
            b = response.content
            with open('image.png', 'wb') as f:
                f.write(b)

            self.pixmap = QPixmap.fromImage(QImage('image.png'))
            self.image.setPixmap(self.pixmap)
            # Создадим картинку
            # и тут же ее покажем встроенным просмотрщиком операционной системы




        except Exception as e:
            self.label.setText('Error', e)

    def keyPressEvent(self, event):
        global now
        if event.key() == Qt.Key_PageDown:
            if now[1] <= 5:
                now = [sps[now[1] + 1], now[1] + 1]
                MyWidget.initUI(self)
        elif event.key() == Qt.Key_PageUp:
            if 1 <= now[1]:
                now = [sps[now[1] - 1], now[1] - 1]
                MyWidget.initUI(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом: