from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect
from flask import request

from ems import app
from ems import bcrypt
from ems.forms import RegistrationForm
from ems.forms import LoginForm
from ems.forms import AddMarksForm

from ems.models import db
from ems.models import User
from ems.models import Marks

from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/dashboard')
def dashboard():
    marks = Marks.query.all()
    return render_template('dashboard.html', marks=marks)


@app.route('/add/marks', methods=['GET', 'POST'])
def addmarks():
    form = AddMarksForm()
    if form.validate_on_submit():
        marks = Marks(roll_id=form.roll_id.data, classname=form.classname.data, name=form.name.data, bengali=form.bengali.data, bengali2=form.bengali2.data, english=form.english.data, english2=form.english2.data, mathematics=form.mathematics.data, science=form.science.data, bandg=form.bandg.data, religion=form.religion.data, total=form.total.data)
        db.session.add(marks)
        db.session.commit()
        flash('Marks sucessfully added for {form.name.data}', 'success')
        return redirect(url_for('addmarks'))
    return render_template('addmarks.html', form=form)