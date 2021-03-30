# flask_wtf — обертка для wtforms
from flask_wtf import FlaskForm  # основной класс, от которого мы будем наследоваться при создании своей формы.

# типы полей, которые нам пригодятся для создания нашей формы:
# текстовое поле, поле ввода пароля, чекбокс, кнопку отправки данных.
from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import DataRequired  # импортируем проверку - введены ли данные в поле или нет


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])  # form.validate_on_submit()
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


# from loginform import LoginForm
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login2.html', title='Авторизация', form=form)  # login.html



'''
{% extends "base.html" %}

{% block content %}
    <h1>Авторизация</h1>
    <form action="" method="post" novalidate>  <!-- параметр novalidate - проверка на сервере -->
        {{ form.hidden_tag() }}  <!-- form. form.hidden_tag — атрибут, который добавляет в форму токен для защиты от атаки. -->
        <p>
            {{ form.username.label }}<br>
            {{ form.username(class="form-control") }}<br>
            {% for error in form.username.errors %}
                <div class="alert alert-danger" role="alert">
                    {{ error }}
                </div>
            {% endfor %}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(class="form-control", type="password") }}<br>
            {% for error in form.password.errors %}
                <div class="alert alert-danger" role="alert">
                    {{ error }}
                </div>
            {% endfor %}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit(type="submit", class="btn btn-primary") }}</p>
    </form>
{% endblock %}
'''
