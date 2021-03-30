from flask import abort, jsonify
from flask_restful import abort, Resource, reqparse, Api

from data import db_session, users_reqparser
from data.users_reqparser import *
from data.__all_models import *


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"users {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({
            'users': users.to_dict(
                only=('name', 'about', 'email', 'city_from',
                      'hashed_password', 'created_date'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({
            'users': [item.to_dict(
                only=('name', 'about', 'email', 'city_from',
                      'hashed_password', 'created_date')) for item in users]})
    
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            name=args['name'],
            about=args['about'],
            email=args['email'],
            city_from=args['city_from']
        )
        users.set_password(args['password'])
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
