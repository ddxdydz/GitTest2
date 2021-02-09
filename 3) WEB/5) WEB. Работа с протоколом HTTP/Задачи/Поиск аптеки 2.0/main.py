import sys
from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт
import math

import requests
from PIL import Image


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


# приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12

toponym_to_find = " ".join(sys.argv[1:])

# Собираем параметры для запроса к Yandex.Maps.Geosearch:
search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

search_params = {"apikey": api_key,
                 "text": "аптека", "lang": "ru_RU",
                 "ll": toponym_to_find, "type": "biz", "results": 1}
response = requests.get(search_api_server, params=search_params)

if not response:
    print("Ошибка выполнения запроса:")
    print(response.url)
    print("Http статус:", response.status_code, "(", response.reason, ")")

json_response = response.json()  # Преобразуем ответ в json-объект

organization = json_response["features"][0]  # Получаем первую найденную организацию.
org_address = organization["properties"]["CompanyMetaData"]["address"]  # Адрес организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]  # Название организации.
org_time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]  # Время
# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
org_distance = lonlat_distance(point, [float(c) for c in toponym_to_find.split(',')])  # Д
org_point = "{0},{1}".format(point[0], point[1])
delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = {"ll": org_point, "l": "map",
              "pt": f"{toponym_to_find},pma~{org_point},pmb"}
response = requests.get(map_api_server, params=map_params)

print(org_address, org_name, org_time, org_distance, sep='\n')
Image.open(BytesIO(response.content)).show()
