from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm # py3中需要用.forms
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the RegistrationForm
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            password=form.password.data)

        db.session.add(employee)
        db.session.commit()
        flash('你已经成功注册！现在可以登录了')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                     form.password.data):

            login_user(employee)

            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
                
            else:
                return redirect(url_for('home.dashboard'))

        else:
            flash('密码或者邮箱无效')

    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
def logout():
    logout_user()
    flash('你已成功退出登录')

    return redirect(url_for('auth.login'))

