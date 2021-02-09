import requests
import math


def get_coords(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}, 1&format=json"
    response = requests.get(geocoder_request)  # Выполняем запрос
    if response:  # Запрос успешно выполнен, печатаем полученные данные.
        try:
            json_response = response.json()  # Преобразуем ответ в json-объект
            # Получаем первый топоним из ответа геокодера.
            # Согласно описанию ответа, он находится по следующему пути:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            # Печатаем извлечённые из ответа поля:
            return toponym["Point"]["pos"].split()
        except IndexError:
            return None


def lonlat_distance(a, b):

    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = map(float, a)
    b_lon, b_lat = map(float, b)

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


h1 = 525
h1_coords = get_coords('Останкинская телебашня')

input_address = input('Введите адрес или географические координаты искомого объекта: ')
h2_coords = get_coords(input_address)

if input_address is None:
    print('Объект не найден')
else:
    distance = lonlat_distance(h1_coords, h2_coords)
    print('Минимальная высота приёмной антенны (в метрах):',
          distance / 3.6 - h1 ** 0.5)

