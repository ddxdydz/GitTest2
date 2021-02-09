import math


def lonlat_distance(a, b):

    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


'''
в качестве метрики расстояния вам нужно использовать декартову метрику на градусной сетке, 
считая 1 градус по широте равным 111 километрам, а отношение градуса широты и градуса долготы, 
равным косинусу широты.

Итого: 1 грд. широты = 111 км. 1 грд. долготы = 111 км * cos(широты).

Пояснение: На экваторе длина градуса широты и долготы в метрах совпадают, 
и примерно равны 111 километрам (длина экватора примерно 40000 км, поделить на 360 градусов). 

Однако с увеличением широты появляется разница, так как длина окружности по параллели с ростом широты уменьшается. 
Представьте себе сечения земного шара плоскостями, параллельными экватору. 
На полюсах это сечение вырождается в точку касания. 
Поэтому там длина градуса долготы стремится к нулю. 
Несложно заметить, что эта зависимость длины градуса по долготе от широты точки выражается косинусом широты. 
Такой способ вычисления расстояний между точками, заданными широтой и долготой подходит, 
если точки не сильно удалены друг от друга. На больших расстояниях такой метод дает большую погрешность 
и потому неприменим.
'''
