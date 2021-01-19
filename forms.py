from flask_wtf import FlaskForm
from wtforms import StringField, TextField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

class UserForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired()])
    l_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    feedback = TextField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit Feedback')