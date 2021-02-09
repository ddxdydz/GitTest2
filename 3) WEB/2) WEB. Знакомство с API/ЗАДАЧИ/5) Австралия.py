import os
import sys

import pygame
import requests

map_request = "https://static-maps.yandex.ru/1.x/?ll=26.388236,59.916324&z=6&l=map&size=450,450"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((450, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()  # Переключаем экран и ждем закрытия окна.
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)  # Удаляем за собой файл с изображением.
