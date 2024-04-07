from flask_sqlalchemy import SQLAlchemy
from wtforms import PasswordField, StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    
class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    lastname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')