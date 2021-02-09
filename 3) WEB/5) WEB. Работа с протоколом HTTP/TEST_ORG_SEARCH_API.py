import sys
from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image


search_api_server = "https://search-maps.yandex.ru/v1/"  # Поиском по организациям.
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
address_ll = "37.588392,55.734036"
search_params = {"apikey": api_key, "text": "аптека", "lang": "ru_RU", "ll": address_ll, "type": "biz"}
response = requests.get(search_api_server, params=search_params)
if not response:
    print("Ошибка выполнения запроса:")
    print(response.url)
    print("Http статус:", response.status_code, "(", response.reason, ")")
json_response = response.json()  # Преобразуем ответ в json-объект
organization = json_response["features"][0]  # Получаем первую найденную организацию.
org_name = organization["properties"]["CompanyMetaData"]["name"]  # Название организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]  # Адрес организации.
# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])
delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = {"ll": address_ll, "spn": ",".join([delta, delta]),
              "l": "map", "pt": "{0},pm2dgl".format(org_point)}
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()  # Создадим картинку + покаже просмотрщиком ос
