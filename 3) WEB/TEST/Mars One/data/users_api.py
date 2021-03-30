import requests

import flask
from flask import jsonify
from flask import make_response, request, Flask

from . import db_session
from .users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.route('/api/users')
def get_user():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify({
        'users': [item.to_dict(
            only=('name', 'about', 'email', 'city_from',
                  'hashed_password', 'created_date')) 
            for item in users]})


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return jsonify({'error': 'Not found'})
    return jsonify({
        'users': users.to_dict(
            only=('name', 'about', 'email', 'city_from',
                  'hashed_password', 'created_date'))})


@blueprint.route('/api/add_users/<int:users_id>', methods=['POST'])
def create_users(users_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'about', 'email', 'city_from', 'password']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    if db_sess.query(User).filter(User.id == users_id).first():
        return jsonify({'error': 'Id already exists'})

    user = User()
    user.name = request.json['name']
    user.about = request.json['about']
    user.email = request.json['email']
    user.city_from = request.json['city_from']
    user.set_password(request.json['password'])
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return jsonify({'error': 'Not found'})
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['PUT'])
def edit_users(users_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'about', 'email', 'city_from', 'password']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    if db_sess.query(User).filter(User.id == users_id).first():
        return jsonify({'error': 'Id already exists'})

    user = User()
    user.name = request.json['name']
    user.about = request.json['about']
    user.email = request.json['email']
    user.city_from = request.json['city_from']
    user.set_password(request.json['password'])
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users_param/<int:user_id>', methods=['GET'])
def get_users_param(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})

    param = dict()
    param['title'] = 'Nostalgia'
    param['username'] = user.name
    param['city_from'] = user.city_from

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
    geocoder_params = {"apikey": api_key, "geocode": user.city_from, "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        param['url_img'] = ''
        return jsonify(param)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"]
    if not toponym:
        print('Not found')
        param['url_img'] = ''
        return jsonify(param)
    toponym_longitude, toponym_lattitude = toponym[0]["GeoObject"]["Point"]["pos"].split()
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {"ll": ",".join([toponym_longitude, toponym_lattitude]), "l": "sat"}
    response = requests.get(map_api_server, params=map_params)

    param['url_img'] = response.url

    return jsonify(param)
