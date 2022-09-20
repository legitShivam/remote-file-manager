from manager import app
from flask import render_template, redirect, url_for, flash
from manager.models import Setting, User
from manager.forms import RegisterForm, LoginForm
from manager import db

user = User.query.all()[0].name.capitalize()
userName = User.query.all()[0].userName
userID = User.query.all()[0].userID

for settings in Setting.query.all():
    if settings.userID == userID:
        showHiddenFile = settings.showHiddenFile
        rootFolder = settings.rootFolder

@app.route("/")
def home_page():
    return render_template("index.html", user=user)


@app.route("/settings")
def settings_page():
    return render_template("settings.html", user=user, userName=userName, userID=userID, showHiddenFile=showHiddenFile)


@app.route("/help")
def help_page():
    return render_template("help.html", user=user)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        userName = form.userName.data
        password = form.password.data
        confirmPassword = form.confirmPassword.data
        character = form.character.data
        user = User(name=name, userName=userName, password_hash=password, character=character)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:   # If there are no errors i.e error dictionary is empty
        for err_msg in form.errors.values():
            flash(err_msg)
    return render_template('register.html', form=form)


@app.route("/login")
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)
