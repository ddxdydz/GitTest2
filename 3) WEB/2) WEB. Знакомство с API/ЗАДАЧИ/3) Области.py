import requests


def print_full_address(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json"
    response = requests.get(geocoder_request)  # Выполняем запрос
    if response:  # Запрос успешно выполнен, печатаем полученные данные.
        json_response = response.json()  # Преобразуем ответ в json-объект
        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Печатаем извлечённые из ответа поля:
        print(toponym['metaDataProperty']['GeocoderMetaData']['Address']['postal_code'])
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")


print_full_address('Петровки, 38')
