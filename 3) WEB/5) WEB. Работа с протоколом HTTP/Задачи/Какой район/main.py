import sys
import requests

# приложение предполагает запуск:
toponym_to_find = " ".join(sys.argv[1:])
# Собираем параметры для запроса к Yandex.Maps.Geosearch:
search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

search_params = {"apikey": api_key, "text": toponym_to_find,
                 "lang": "ru_RU", "type": "biz", "results": 1}
response = requests.get(search_api_server, params=search_params)

if not response:
    print("Ошибка выполнения запроса:")
    print(response.url)
    print("Http статус:", response.status_code, "(", response.reason, ")")

json_response = response.json()  # Преобразуем ответ в json-объект
organization = json_response["features"][0]  # Получаем первую найденную организацию.
point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])

# Собираем параметры для запроса к Yandex.Maps.Geocoder:
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                   "geocode": org_point, "kind": "district", "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:  # обработка ошибочной ситуации
    pass
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
print(toponym["metaDataProperty"]["GeocoderMetaData"]["text"])
