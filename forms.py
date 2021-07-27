from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


# from flask.ext.admin.form.widgets import DatePickerWidget

class MovieForm(FlaskForm):
    name = StringField('Movie Name', validators=[DataRequired()])
    timing = DateTimeField('Movie Timing', validators=[DataRequired()])
    location = StringField('Movie Location', validators=[DataRequired()])
