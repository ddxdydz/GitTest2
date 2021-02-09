import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [450, 450]


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.map_files = []
        self.cur_img = 0
        self.getImages("https://static-maps.yandex.ru/1.x/?ll=37.617635,55.755814&z=10&l=map&size=450,450&pt=37.55,55.71,comma~37.43,55.81,comma~37.55,55.78,comma",
                       "https://static-maps.yandex.ru/1.x/?ll=26.388236,59.916324&z=6&l=map&size=450,450&pl=30.315868,59.939095,28.379801,60.020732,24.513118,59.563466,18.791369,59.280390",
                       "https://static-maps.yandex.ru/1.x/?ll=134.019322,-24.927056&z=3&l=map&size=450,450",
                       "https://static-maps.yandex.ru/1.x/?ll=134.019322,-24.927056&z=0&l=map&size=450,450")
        self.initUI()

    def getImages(self, *map_requests):
        number = 0
        for map_request in map_requests:
            response = requests.get(map_request)
            if not response:
                print("Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            # Запишем полученное изображение в файл.
            map_file = f"map{number}.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            self.map_files.append(map_file)
            number += 1

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)  # x, y, width, height
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('Отображение карты')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(450, 450)
        self.update_image()

    def update_image(self):
        self.pixmap = QPixmap(self.map_files[self.cur_img])
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, QKeyEvent):
        self.cur_img = (self.cur_img + 1) % len(self.map_files)
        self.update_image()
        print(self.cur_img)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        for map_file in self.map_files:
            os.remove(map_file)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
