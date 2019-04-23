from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import ValidationError
from wtforms import validators
from wtforms.validators import DataRequired


def validate_name(form, field):
    for i in field.data:
        if i == ' ':
            raise ValidationError('Name should not contain white space.')
        if not i.isalnum():
            raise ValidationError(
                'Name should not contain special character',
            )


def validate_passphrase(form, field):
    has_alpha = False
    has_num = False
    for i in field.data:
        if i.isnumeric():
            has_num = True
        if i.isalpha():
            has_alpha = True
    if not has_alpha or not has_num:
        raise ValidationError(
            "Password must have both letters and numbers!",
        )


class RegisterForm(FlaskForm):
    name = StringField(
        'Name', validators=[
            DataRequired(),
            validators.length(min=4, max=20),
            validate_name,
        ],
    )
    passphrase = StringField(
        'Passphrase', validators=[
            DataRequired(),
            validate_passphrase,
        ],
    )
    confirm = SubmitField('Confirm')
    address = StringField('Address')
