import flask
from flask import jsonify
from flask import make_response, request, Flask

from . import db_session
from .jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.route('/api/jobs')
def get_job():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify({
        'jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size',
                  'collaborators', 'start_date', 'end_date',
                  'category', 'is_finished'))
                 for item in jobs]})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify({
        'jobs': jobs.to_dict(
            only=('team_leader', 'job', 'work_size',
                  'collaborators', 'start_date', 'end_date',
                  'category', 'is_finished'))})


@blueprint.route('/api/add_jobs/<int:jobs_id>', methods=['POST'])
def create_jobs(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size',
                  'collaborators', 'start_date', 'end_date',
                  'category', 'is_finished']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    if db_sess.query(Jobs).filter(Jobs.id == jobs_id).first():
        return jsonify({'error': 'Id already exists'})

    jobs = Jobs()
    jobs.team_leader = request.json['team_leader']
    jobs.job = request.json['job']
    jobs.work_size = request.json['work_size']
    jobs.collaborators = request.json['collaborators']
    jobs.start_date = request.json['start_date']
    jobs.end_date = request.json['end_date']
    jobs.category = request.json['category']
    jobs.is_finished = request.json['is_finished']
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_jobs(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size',
                  'collaborators', 'start_date', 'end_date',
                  'category', 'is_finished']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    if db_sess.query(Jobs).filter(Jobs.id == jobs_id).first():
        return jsonify({'error': 'Id already exists'})

    jobs = Jobs()
    jobs.team_leader = request.json['team_leader']
    jobs.job = request.json['job']
    jobs.work_size = request.json['work_size']
    jobs.collaborators = request.json['collaborators']
    jobs.start_date = request.json['start_date']
    jobs.end_date = request.json['end_date']
    jobs.category = request.json['category']
    jobs.is_finished = request.json['is_finished']
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})
