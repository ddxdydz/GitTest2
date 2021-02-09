import os
import sys
from random import choice

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import uic

from PIL import Image
from PIL.ImageQt import ImageQt

from io import BytesIO
from PIL import Image

MAP_SIZE = ['600', '400']


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('form.ui', self)

        self.map_api_server = "http://static-maps.yandex.ru/1.x/"

        self.map_params = {"ll": "0,0", "l": 'map', "size": ','.join(MAP_SIZE),
                           "spn": "180,90", "lang": 'tr_UA'}

        self.towns_list = None

        self.btn.clicked.connect(self.press_button)

        self.map_file = self.getImage()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Угадай-ка город')
        self.setFixedSize(self.width(), self.height())
        with open('towns_list.txt', mode='rt', encoding='UTF-8') as file:
            self.towns_list = file.read().split('\n')
        self.set_default_values()
        self.search_random_town()

    def press_button(self):
        if self.btn.text() == 'SHOW TOWN NAME':
            self.town_name.setVisible(True)
            self.btn.setText('NEXT')
        else:
            self.set_default_values()
            self.search_random_town()

    def getImage(self):
        response = requests.get(self.map_api_server, params=self.map_params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(response.url)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Write the resulting image to a file.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

        if 'sat' in self.map_params['l']:
            # Load image
            im = Image.open(map_file)
            # Convert to palette mode and save
            im.convert('P').save(map_file)

        return map_file

    def update_map(self):
        self.map_file = self.getImage()
        self.map_label.setPixmap(QPixmap(self.map_file))

    def set_default_values(self):
        self.btn.setText('SHOW TOWN NAME')
        self.town_name.setVisible(False)

    def search_random_town(self):
        cur_town = choice(self.towns_list)

        # Собираем параметры для запроса к Yandex.Maps.Geocoder:
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                           "geocode": cur_town, "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

        self.map_params["ll"] = ','.join([toponym_longitude, toponym_lattitude])
        self.map_params["l"] = choice(['map', 'sat'])
        self.map_params["spn"] = self.get_spn(toponym)
        self.town_name.setText(cur_town)

        self.update_map()

    def get_spn(self, tm):
        lowerCorner, upperCorner = [v.split() for v in tm[
            "boundedBy"]["Envelope"].values()]
        spn_delta_1 = float(upperCorner[0]) - float(lowerCorner[0])
        spn_delta_2 = float(upperCorner[1]) - float(lowerCorner[1])
        return f"{str(spn_delta_1 / 10)},{str(spn_delta_2 / 10)}"

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
