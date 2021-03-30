from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = StringField('team_leader', validators=[DataRequired()])
    job = TextAreaField("job")
    work_size = StringField('work_size', validators=[DataRequired()])
    collaborators = StringField('collaborators', validators=[DataRequired()])
    start_date = StringField('start_date', validators=[DataRequired()])
    end_date = StringField('end_date', validators=[DataRequired()])
    category = StringField('category')
    is_finished = BooleanField("is_finished")
    submit = SubmitField('Submit')
