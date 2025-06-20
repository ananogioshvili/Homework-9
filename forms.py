from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField,
                            SelectField, DateField, IntegerField,
                            RadioField, SubmitField)
from wtforms.validators import DataRequired, length


class SignUpForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    surname = StringField("Surname:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    phone = IntegerField("+995 555 55 55 55", validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    country = SelectField(choices=["Choose country:", "Georgia", "Italy", "Spain", "France"], validators=[DataRequired()])
    gender = RadioField("Choose gender:", choices=["Male", "Female"], validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired(), length(min=8, max=20)])

    submit = SubmitField("Sign up")

