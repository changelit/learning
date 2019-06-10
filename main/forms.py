from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


def is_42(message=None):
    if message is None:
        message = 'Must be 42'

    def _is_42(form, field):
        if field.data != 42:
            raise ValidationError(message)

    return _is_42


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    photo = FileField('Upload image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    password = PasswordField('Password', validators=[DataRequired('Password is required'), Length(8, 30)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
