import requests


def upgrade_address(address, bbox=''):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&bbox={bbox}&format=json"
    response = requests.get(geocoder_request)  # Выполняем запрос
    if response:  # Запрос успешно выполнен, печатаем полученные данные.
        try:
            json_response = response.json()  # Преобразуем ответ в json-объект
            # Получаем первый топоним из ответа геокодера.
            # Согласно описанию ответа, он находится по следующему пути:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            # Полный адрес топонима:
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            # Печатаем извлечённые из ответа поля:
            return toponym_address
        except IndexError:
            return None


result = None
bbox_step = 10

while True:
    address_cords = input('Долгота и широта точки через пробел:').split()
    try:
        if len(address_cords) == 2:
            address_cords = (float(address_cords[0]), float(address_cords[1]))
            if -180 <= address_cords[0] <= 180 and -90 <= address_cords[1] <= 90:
                address_cords = (address_cords[0], address_cords[1], address_cords[0], address_cords[1])
                break
    except ValueError:
        pass
    print('Неверный формат введённых данных')

while result is None:
    lon1, lat1, lon2, lat2 = \
        (address_cords[0] - bbox_step, address_cords[1] - bbox_step,
         address_cords[2] + bbox_step, address_cords[3] + bbox_step)
    lon1 = (180 + lon1) if lon1 < -90 else lon1
    lat1 = (360 + lat1) if lat1 < -180 else lat1
    lon2 = (-180 + lon2) if lon2 > 90 else lon2
    lat2 = (-360 + lat2) if lat2 > 180 else lat2
    address_cords = lon1, lat1, lon2, lat2
    print(address_cords)
    result = upgrade_address('станция метро', bbox=f'{address_cords[0]},{address_cords[1]}~{address_cords[2]},{address_cords[3]}')
print(result)


# 37.621269 55.752157
# -100.835661 39.797613
# -169.805916 80.027876
# 40.805664 56.965538
# 18.907694 52.529863
