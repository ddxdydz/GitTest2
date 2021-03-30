from flask import abort, jsonify
from flask_restful import abort, Resource, reqparse, Api

from data import db_session, jobs_reqparser
from data.jobs_reqparser import *
from data.__all_models import *


# app = Flask(__name__)
# api = Api(app)

# api.add_resource(news_resources.NewsListResource, '/api/v2/news')  # для списка объектов
# api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')  # для одного объекта


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"jobs {jobs_id} not found")


class JobsResource(Resource):
    #  get, put, post, delete - должны принимать в качестве аргумента идентификатор объекта.
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({
            'jobs': jobs.to_dict(
                only=('team_leader', 'job', 'work_size',
                      'collaborators', 'start_date', 'end_date',
                      'category', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    # get и post без аргументов.
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({
            'jobs': [item.to_dict(
                only=('team_leader', 'job', 'work_size',
                      'collaborators', 'start_date', 'end_date',
                      'category', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            category=args['category'],
            is_finished=args['is_finished']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

