import sys
from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт
import math

import requests
from PIL import Image


# приложение предполагает запуск: python search.py 34,58
toponym_to_find = " ".join(sys.argv[1:])

# Собираем параметры для запроса к Yandex.Maps.Geosearch:
search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
search_params = {"apikey": api_key,
                 "text": "аптека", "lang": "ru_RU",
                 "ll": toponym_to_find, "type": "biz", "results": 10, 'spn': '180,90'}
response = requests.get(search_api_server, params=search_params)
if not response:
    print("Ошибка выполнения запроса:")
    print(response.url)
    print("Http статус:", response.status_code, "(", response.reason, ")")

json_response = response.json()  # Преобразуем ответ в json-объект

cur_pts = []
for organization in json_response["features"]:
    org_time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]  # Время
    # Получаем координаты ответа.
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])

    if not len(org_time):
        cur_pts.append(f"{org_point},pmgrs")
    elif 'круглосуточно' in org_time:
        cur_pts.append(f"{org_point},pmgns")
    else:
        cur_pts.append(f"{org_point},pmbls")

# Собираем параметры для запроса к StaticMapsAPI:
map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = {"l": "map", "pt": '~'.join(cur_pts)}
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
