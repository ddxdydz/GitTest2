import requests


def print_full_address(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}, 1&format=json"
    response = requests.get(geocoder_request)  # Выполняем запрос
    if response:  # Запрос успешно выполнен, печатаем полученные данные.
        json_response = response.json()  # Преобразуем ответ в json-объект
        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Печатаем извлечённые из ответа поля:
        # print(toponym_address, "имеет координаты:")
        print(address, '-', toponym['metaDataProperty']['GeocoderMetaData']['Address']['Components'][1]['name'])
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")


for town in ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']:
    print_full_address(town)
