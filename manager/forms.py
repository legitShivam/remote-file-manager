from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    name = StringField(label='Name')
    userName = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    character = StringField(label='Character')
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    confirmPassword =PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    userName = StringField(label='Username')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Submit')