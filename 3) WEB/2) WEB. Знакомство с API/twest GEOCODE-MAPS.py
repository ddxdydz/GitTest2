import requests

'''
Функция get() >>> requests.models.Response:
- content — ответ сервера
- json_response = response.json()  # Преобразуем ответ в json-объект  
- _bool_() - возвращающий True в случае успешного запроса и False
- status_code — код статуса (200 означает, что запрос выполнен успешно)
- reason — текстовая расшифровка статуса на английском языке (например, «Ok» или «Not Found»)
'''

import requests

# Yandex.Maps.StaticAPI
map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
else: 
    # Запишем полученное изображение в файл.
    self.map_file = "map.png"
    with open(self.map_file, "wb") as file:
        file.write(response.content)
    # PyGame - screen.blit(pygame.image.load(map_file), (0, 0))
    # PyQt5 - self.pixmap = QPixmap(self.map_file)

# Yandex.Maps.Geocoder
geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=станция Метро&format=json"
response = requests.get(geocoder_request)  # Выполняем запрос. Для выполнения запроса GET
if response:  # Запрос успешно выполнен, печатаем полученные данные.
    json_response = response.json()  # Преобразуем ответ в json-объект
    # Получаем 1ый топоним из ответа геокодера:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]  # Полный адрес топонима:
    toponym_coodrinates = toponym["Point"]["pos"]  # Координаты центра топонима:
    print(toponym_address, "имеет координаты:", toponym_coodrinates)  # Печатаем извлечённые из ответа поля:
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
