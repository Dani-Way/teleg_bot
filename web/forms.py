from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# //DataRequired = должен быть хотя бы один символ
# Length = длина строки от 2 до 20
# Email = проверка на введён ли емаил
# EqualTo = сравнивает данные в двух полях


# Форма регистрации
class RegisterForm(FlaskForm):
	username 			= StringField("Псевдоним",validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder":"Псевдоним"})
	email				= StringField("Почта",validators=[DataRequired(),Email(message="Невалидный адрес электронной почты."),validate_email(exist=False)],render_kw={"placeholder":"Почта"})
	password 			= PasswordField("Пароль",validators=[DataRequired(),password_check],render_kw={"placeholder":"Пароль"})
	confirm_password 	= PasswordField("Пароль ещё раз",validators=[DataRequired(),EqualTo("password",message="Пароли должны совпадать")],render_kw={"placeholder":"Пароль ещё раз"})
	submit 				= SubmitField("Зарегистрироваться")

# Форма входа
class LoginForm(FlaskForm):
	email 		= StringField("Почта",validators=[DataRequired(),Email(message="Невалидный адрес электронной почты.")],render_kw={"placeholder":"Почта"})
	password 	= PasswordField("Пароль",validators=[DataRequired()],render_kw={"placeholder":"Пароль"})
	remember 	= BooleanField("Запомнить меня")
	submit 		= SubmitField("Войти")

# Форма забыл пароль
class ForgotPasswordForm(FlaskForm):
	email 		= StringField("Почта",validators=[DataRequired(),Email(message="Невалидный адрес электронной почты."),validate_email()],render_kw={"placeholder":"Почта"})
	submit 		= SubmitField("Отправить")

# Форма обмена
class ChangeForm(FlaskForm):
	received_currency 	= StringField("Валюта",validators=[DataRequired()],render_kw={"placeholder":"Валюта"})
	received_nominal 	= StringField("Сумма",validators=[DataRequired(), Length(min=1,max=8)],render_kw={"placeholder":"Валюта"})
	return_currency 	= StringField("Валюта",validators=[DataRequired()],render_kw={"placeholder":"Валюта"})
	return_nominal 		= StringField("Сумма",validators=[DataRequired(), Length(min=1,max=8)],render_kw={"placeholder":"Валюта"})
	email 				= StringField("Почта",validators=[DataRequired(),Email(message="Невалидный адрес электронной почты.")],render_kw={"placeholder":"Почта"})
	number				= StringField("Номер карты",validators=[DataRequired()],render_kw={"placeholder":"Номер карты"})
	submit 				= SubmitField("Обменять")



