from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()],
                           render_kw={"placeholder": "Введите имя", 'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()],
                             render_kw={"placeholder": "Введите пароль", 'class': 'form-control'})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})


class ReistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()],
                           render_kw={"placeholder": "Введите имя", 'class': 'form-control'})
    email = StringField('Электорнная почта', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Введите email", 'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()],
                             render_kw={"placeholder": "Введите пароль", 'class': 'form-control'})
    password2 = PasswordField('Пароль', validators=[DataRequired(), EqualTo('password')],
                              render_kw={"placeholder": "Повторите пароль", 'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
