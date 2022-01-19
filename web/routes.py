from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

from portfolium import app, db, mail, HOST
from portfolium.forms import RegisterForm, LoginForm, ForgotPasswordForm, ChangeForm
# from portfolium.models import User, Portfolio, ConfirmRequest, ResetPasswordRequest