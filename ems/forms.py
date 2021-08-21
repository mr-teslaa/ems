from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators = [
            DataRequired(),
            Length(min=2, max=20)
        ]
    )

    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators = [
            DataRequired()
            ]
        )

    confirm_password = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators = [
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')



class AddMarksForm(FlaskForm):
    roll_id = IntegerField(
        'Roll / ID',
        validators = [ DataRequired() ]
    )

    classname = StringField(
        'Class Name',
        validators = [ DataRequired() ]
    )

    name = StringField(
        'Student\'s Name',
        validators = [ DataRequired() ]
    )

    bengali = IntegerField(
        'Bengali',
        validators = [ DataRequired() ]
    )

    bengali2 = IntegerField(
        'Bengali 2',
        validators = [ DataRequired() ]
    )

    english = IntegerField(
        'English',
        validators = [ DataRequired() ]
    )

    english2 = IntegerField(
        'English 2',
        validators = [ DataRequired() ]
    )

    mathematics = IntegerField(
        'Mathematics',
        validators = [ DataRequired() ]
    )

    science = IntegerField(
        'Science',
        validators = [ DataRequired() ]
    )

    bandg = IntegerField(
        'B & G',
        validators = [ DataRequired() ]
    )

    religion = IntegerField(
        'Religion',
        validators = [ DataRequired() ]
    )

    total = IntegerField(
        'Total',
        validators = [ DataRequired() ]
    )

    submit = SubmitField('Submit')
