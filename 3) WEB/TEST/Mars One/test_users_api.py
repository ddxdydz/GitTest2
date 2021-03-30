from requests import get, post, delete, put

print(get('http://localhost:8000/api/v2/users/1').json())
# с id = 999 нет в базе
print(get('http://localhost:8000/api/v2/users/999').json())
# аргумент в виде строки
print(get('http://localhost:8000/api/v2/users/b'))

print(delete('http://localhost:8000/api/v2/users/1').json())
# с id = 999 нет в базе
print(delete('http://localhost:8000/api/v2/users/999').json())

print(get('http://localhost:8000/api/v2/users').json())

print(post('http://localhost:8000/api/v2/users', json={
    'name': 'TEST USER',
    'about': 'TEST USER',
    'email': 'TEST@TEST',
    'city_from': 'TEST',
    'password': 'TEST USER'
}))
# не хватает параметра
print(post('http://localhost:8000/api/v2/users', json={
    'name': 'TEST USER',
    'about': 'TEST USER',
    'email': 'TEST@TEST',
    'password': 'TEST USER'
}).json())
# пустой json
print(post('http://localhost:8000/api/v2/users', json={}).json())

