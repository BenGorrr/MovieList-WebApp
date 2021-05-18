from flask import render_template, url_for, redirect, flash
from app import app
from app.forms import RegistrationForm, LoginForm

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Logged in as {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
