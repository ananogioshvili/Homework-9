from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields import (StringField, PasswordField,
                            SelectField, DateField, IntegerField,
                            RadioField, SubmitField, FileField,)
from wtforms.validators import DataRequired, length


class SignUpForm(FlaskForm):
    image = FileField(validators=[FileRequired()])
    name = StringField("Name:", validators=[DataRequired()])
    surname = StringField("Surname:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    phone = IntegerField("+995 555 55 55 55", validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    country = SelectField(choices=["Choose country:", "Georgia", "Italy", "Spain", "France"], validators=[DataRequired()])
    gender = RadioField("Choose gender:", choices=["Male", "Female"], validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired(), length(min=8, max=20)])

    submit = SubmitField("Sign up")



class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])

    submit = SubmitField("Login")


class ProductForm(FlaskForm):
    image = FileField("Add product photo", validators=[FileAllowed(["jpg", "jpeg", "png", "gif"])])
    name = StringField("Add product name", validators=[DataRequired()])
    price = IntegerField("Add product price", validators=[DataRequired()])

    submit = SubmitField("Add product")
