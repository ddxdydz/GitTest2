import os
import sys

import pygame
import requests


map_file = None


def get_image(lon1, lat1, lon2, lat2):
    global map_file
    map_request = f"https://static-maps.yandex.ru/1.x/?ll=-169.805916,80.027876&z=1&l=map&size=450,450&pl=c:ec473fFF,f:00FF00A0, w:7,{lon1},{lat1},{lon1},{lat2},{lon2},{lat1},{lon2},{lat2}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((450, 450))
get_image(164.736666, 82.400640, -153.926536, 77.698960)
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()  # Переключаем экран и ждем закрытия окна.
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)  # Удаляем за собой файл с изображением.
