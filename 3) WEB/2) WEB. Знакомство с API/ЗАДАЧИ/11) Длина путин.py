import os
import sys
import math

import pygame
import requests


points = [-87.931990, 38.309591, -4.042824, 28.848145,
          43.127566, 34.522412, 24.672970, 43.803956,
          10.788687, 51.613616, 26.084091, 68.658881,
          103.606057, 58.250201, 111.870212, 29.700531,
          137.712491, -26.584903, 47.539145, -18.092017]


def get_image(point_cords):
    map_request = f"https://static-maps.yandex.ru/1.x/?ll=0,0&z=1&l=map&size=450,450&pl={','.join(point_cords)}&pt={','.join(point_cords[len(point_cords) // 2:len(point_cords) // 2 + 2])},comma"
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
    return map_file


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


pygame.init()
screen = pygame.display.set_mode((450, 450))
map_file = get_image([str(elem) for elem in points])
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
print(sum([lonlat_distance(
    (points[i], points[i + 1]),
    (points[i + 2], points[i + 3]))
    for i in range(0, len(points), 4)]), 'м')
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)  # Удаляем за собой файл с изображением.
