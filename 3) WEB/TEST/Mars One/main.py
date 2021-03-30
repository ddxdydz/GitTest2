import datetime
from requests import get

from flask import Flask, request, render_template, redirect, abort, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import reqparse, abort, Api, Resource

from data import db_session, jobs_api, users_api, jobs_resources, users_resources
from data.__all_models import *
from forms.login import LoginForm
from forms.jobs import JobsForm
from forms.user import RegisterForm
from forms.deps import DepartmentsForm
from forms.cats import CategoriesForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

api = Api(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        jobs = db_sess.query(Jobs).all()
        return render_template("index.html", jobs=jobs)
    return redirect("/login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template(
                'register.html', title='Регистрация', form=form,
                message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template(
                'register.html', title='Регистрация', form=form,
                message="Такой пользователь уже есть")
        user = User(name=form.name.data, email=form.email.data, about=form.about.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required  # может попасть только авторизованный пользователь
def logout():
    logout_user()
    return redirect("/")


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.start_date = form.start_date.data
        job.end_date = form.end_date.data
        job.category = form.category.data
        job.is_finished = form.is_finished.data
        current_user.jobs.append(job)
        db_sess.merge(current_user)  # изменили пользователя
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление работы', form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).filter(
            Jobs.collaborators.like(f"%{current_user.id}%") | Jobs.collaborators.like(
                f"%{1}%")).first()
        if jobs:
            form.team_leader.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.start_date.data = jobs.start_date
            form.end_date.data = jobs.end_date
            form.category.data = jobs.category
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).filter(
            Jobs.collaborators.like(f"%{current_user.id}%") | Jobs.collaborators.like(
                f"%{1}%")).first()
        if jobs:
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.start_date = form.start_date.data
            jobs.end_date = form.end_date.data
            form.category.data = jobs.category
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html', title='Редактирование новости', form=form)


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id).filter(
        Jobs.collaborators.like(f"%{current_user.id}%") | Jobs.collaborators.like(f"%{1}%")).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route("/departments")
def departments():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        deps = db_sess.query(Department).all()
        return render_template("deps_index.html", deps=deps)
    return redirect("/login")


@app.route('/deps',  methods=['GET', 'POST'])
@login_required
def add_deps():
    form = DepartmentsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dep = Department()
        dep.title = form.title.data
        dep.chief = form.chief.data
        dep.members = form.members.data
        dep.email = form.email.data
        db_sess.add(dep)
        db_sess.commit()
        return redirect('/departments')
    return render_template('deps.html', title='Добавление департамента', form=form)


@app.route('/deps/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_deps(id):
    form = DepartmentsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        deps = db_sess.query(Department).filter(Department.id == id).first()
        if deps:
            form.title.data = deps.title
            form.chief.data = deps.chief
            form.members.data = deps.members
            form.email.data = deps.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        deps = db_sess.query(Department).filter(Department.id == id).first()
        if deps:
            deps.title = form.title.data
            deps.chief = form.chief.data
            deps.members = form.members.data
            deps.email = form.email.data
            db_sess.add(deps)
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('deps.html', title='Редактирование департамента', form=form)


@app.route('/deps_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deps_delete(id):
    db_sess = db_session.create_session()
    deps = db_sess.query(Department).filter(Department.id == id).first()
    if deps:
        db_sess.delete(deps)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


@app.route("/categories")
def categories():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        cats = db_sess.query(Category).all()
        return render_template("cats_index.html", cats=cats)
    return redirect("/login")


@app.route('/cats',  methods=['GET', 'POST'])
@login_required
def add_cats():
    form = CategoriesForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        cat = Category()
        cat.name = form.name.data
        db_sess.add(cat)
        db_sess.commit()
        return redirect('/categories')
    return render_template('cats.html', title='Добавление категории', form=form)


@app.route('/cats/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_cats(id):
    form = CategoriesForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        cats = db_sess.query(Category).filter(Category.id == id).first()
        if cats:
            form.name.data = cats.name
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        cats = db_sess.query(Category).filter(Category.id == id).first()
        if cats:
            form.name.data = cats.name
            db_sess.add(cats)
            db_sess.commit()
            return redirect('/categories')
        else:
            abort(404)
    return render_template('cats.html', title='Редактирование категорий', form=form)


@app.route('/cats_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def cats_delete(id):
    db_sess = db_session.create_session()
    cats = db_sess.query(Category).filter(Category.id == id).first()
    if cats:
        db_sess.delete(cats)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/categories')


@app.route('/users_show/<int:user_id>')
@login_required
def users_show(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return f"The user with id = {user_id} was not found."

    param = get(f'http://localhost:8000/api/users_param/{user_id}').json()

    return render_template('users_show.html', **param)  # HTML-шаблон


def main():  # http://127.0.0.1:8000/
    db_session.global_init("db/blogs.db")

    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)

    api.add_resource(jobs_resources.JobsResource, '/api/v2/jobs/<int:jobs_id>')  # для одного объекта
    api.add_resource(jobs_resources.JobsListResource, '/api/v2/jobs')  # для списка объектов

    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:users_id>')  # для одного объекта
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')  # для списка объектов

    app.run(port=8000, host='127.0.0.1')


if __name__ == '__main__':
    main()
