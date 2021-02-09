import requests


def get_coord(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}, 1&format=json"
    response = requests.get(geocoder_request)  # Выполняем запрос
    if response:  # Запрос успешно выполнен, печатаем полученные данные.
        try:
            json_response = response.json()  # Преобразуем ответ в json-объект
            # Получаем первый топоним из ответа геокодера.
            # Согласно описанию ответа, он находится по следующему пути:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            # Печатаем извлечённые из ответа поля:
            return toponym["Point"]["pos"].split()[1]
        except IndexError:
            return None


print('Cписок городов вводится с клавиатуры через запятую.')
town_list = input('ВВОД: ').split(',')
town_list = map(lambda elem: (elem, get_coord(elem)), town_list)
town_list = filter(lambda elem: elem[1] is not None, town_list)
print(min(town_list, key=lambda elem: float(elem[1]))[0])
