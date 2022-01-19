from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

from time import time
import bcrypt
import secrets
import json

from portfolium import app, db, mail, HOST
from portfolium.forms import RegisterForm, LoginForm, ForgotPasswordForm, ChangeForm
# from portfolium.models import User, Portfolio, ConfirmRequest, ResetPasswordRequest

# Путь формы регистрации
@app.route("/register",methods=["GET","POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = RegisterForm()
	if form.validate_on_submit():
		confirm_request = ConfirmRequest.query.filter_by(email=form.email.data).first()
		if confirm_request:
			confirm_request.username = form.username.data
			confirm_request.password = bcrypt.hashpw(
		        form.password.data.encode(),
		        bcrypt.gensalt()
		    ) 
			confirm_request.hash = secrets.token_hex(8)
		else:
			db.session.add(ConfirmRequest(
			    username = form.username.data,
			    email = form.email.data,
			    password =  bcrypt.hashpw(
			        form.password.data.encode(),
			        bcrypt.gensalt()
			    ),
			    hash = secrets.token_hex(8) 
			))
			confirm_request = ConfirmRequest.query.filter_by(email=form.email.data).first()
		msg = Message(
			sender=app.config.get("MAIL_USERNAME"),
			recipients=[form.email.data],
			subject="Portfolium",
			html=render_template("mail/confirm.html",data=confirm_request,url=HOST))
		mail.send(msg)
		db.session.commit()
		flash("Вам на почту отправлено письмо с ссылкой на подтверждение аккаунта","success")
		return(redirect(url_for("login")))
	return render_template("register.html",form=form)


# Путь формы авторизации
@app.route("/login",methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.checkpw(form.password.data.encode(),user.password.encode()):
			login_user(user, remember=form.remember.data)
			return redirect(url_for("index"))
		else:
			flash("Вы ввели неверные данные.","warning")
	return render_template("login.html",form=form)


# Путь формы забыл пароль
@app.route("/forgot_password",methods=["GET","POST"])
def forgot_password():
	form = ForgotPasswordForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		reset_password_request = ResetPasswordRequest.query.filter_by(owner_id=user.id).first()
		if reset_password_request:
			reset_password_request.owner_id = user.id 
			reset_password_request.hash = secrets.token_hex(8)
		else:
			db.session.add(ResetPasswordRequest(
			    owner_id = user.id,
			    hash = secrets.token_hex(8) 
			))
			reset_password_request = ResetPasswordRequest.query.filter_by(owner_id=user.id).first()
		db.session.commit()
		msg = Message(
			sender=app.config.get("MAIL_USERNAME"),
			recipients=[form.email.data],
			subject="Portfolium",
			html=render_template("mail/reset_password.html",data=reset_password_request,url=HOST))
		mail.send(msg)
		flash(f"На почту ({form.email.data}) отправлено письмо с нужной ссылкой","success")
	return render_template("forgot-password.html",form=form)

# Путь формы обмена
@app.route("/сhangeForm",methods=["GET","POST"])
def сhangeForm():
	form = ChangeForm()




@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

@app.context_processor
def inject_debug():
    return dict(debug=app.debug)



