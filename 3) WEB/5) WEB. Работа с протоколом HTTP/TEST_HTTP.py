import sys
from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

# "https://search-maps.yandex.ru/v1/"
# "http://geocode-maps.yandex.ru/1.x/"  api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
# "http://static-maps.yandex.ru/1.x/"  api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
'''
params = {'list_param': ['value1', 'value2']}
response = requests.get('адрес_сайта', params=params)  # адрес_сайта?list_param=value1&list_param=value2
print(response.url)  # Посмотреть получившийся запрос можно с помощью атрибута url:

# Задать заголовки можно с помощью параметра headers:
headers = {'user-agent': 'yandexlyceum/1.1.1'}
response = requests.get(url, headers=headers)
'''
delta = "0.005"
# python search.py Москва, ул. Ак. Королева, 12
toponym_to_find = " ".join(sys.argv[1:])  # формируется запрос к геокодеру


# Собираем параметры для запроса к Yandex.Maps.Geosearch:
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


# Собираем параметры для запроса к Yandex.Maps.Geocoder:
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
geocoder_params = {"apikey": api_key, "geocode": toponym_to_find, "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)  # Выполняем запрос. Для выполнения запроса GET
if not response:  # обработка ошибочной ситуации
    print("Ошибка выполнения запроса:")
    print(response.url)
    print("Http статус:", response.status_code, "(", response.reason, ")")
json_response = response.json()  # Преобразуем ответ в json-объект
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]  # Получаем топоним
toponym_longitude, toponym_lattitude = toponym["Point"]["pos"].split()  # Долгота и широта
'''geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Метро&format=json"
response = requests.get(geocoder_request)'''


# Собираем параметры для запроса к Yandex.Maps.StaticAPI:
map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = {"ll": ",".join([toponym_longitude, toponym_lattitude]),
              "spn": ",".join([delta, delta]), "l": "map"}
response = requests.get(map_api_server, params=map_params)  # выполняем запрос
'''map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
# Запишем полученное изображение в файл.
self.map_file = "map.png"
with open(self.map_file, "wb") as file:
    file.write(response.content)
# PyGame - screen.blit(pygame.image.load(map_file), (0, 0))
# PyQt5 - self.pixmap = QPixmap(self.map_file)'''


Image.open(BytesIO(response.content)).show()  # Создадим картинку + покаже просмотрщиком ос
