from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class DepartmentsForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    chief = StringField('chief', validators=[DataRequired()])
    members = StringField('members', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    submit = SubmitField('Submit')
