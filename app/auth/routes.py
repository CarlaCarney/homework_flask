from fileinput import filename
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UserCreationForm, LoginForm
from app.models import User
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=["GET", "POST"])
def signupPage():
    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)
            user.saveToDB()

            return redirect(url_for('auth.loginPage'))
    return render_template('signup.html', form=form)


@auth.route('/login', methods=["GET","POST"])
def loginPage():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
            if user:
            
                if check_password_hash(user.password, password):
                    print('succesfully logged in')
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    print('incorrect password')

            else:
                print('user does not exist')


    return render_template('login.html', form=form)


@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.loginPage'))