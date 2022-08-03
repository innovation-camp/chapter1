import hashlib

from flask import Blueprint, render_template, request, g, redirect, url_for, flash

from app.db import get_db
from app.decorators.login_required import login_required

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/')
@login_required
def account_test():
    return "hi"


@bp.route('/signup')
def signup():
    return render_template('account/signup.html')


@bp.route('/signin')
def signin():
    return render_template('account/signin.html')


@bp.route('/api/signup', methods=['POST'])
def api_signup():
    email = request.form.get('usermail')
    password = request.form.get('userpw')
    password_check = request.form.get('userpwcheck')
    nickname = request.form.get('usernickname')

    if not email:
        flash('이메일을 입력해주세요.')
        return render_template('account/signup.html')

    if len(email.split('@')) < 2:
        flash('올바른 이메일 형식이 아닙니다.')
        return render_template('account/signup.html')

    db = get_db()
    user = db.user.find_one({"email": email})

    if user:
        flash('중복된 이메일입니다.')
        return render_template('account/signup.html')

    if password != password_check:
        flash('비밀번호가 일치하지 않습니다.')
        return render_template('account/signup.html')

    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    db.user.insert_one({"email": email, "password": hashed_password, "nickname": nickname})
    return redirect(url_for('account.signin'))


@bp.route('/api/signin')
def api_signin():


    return render_template('account/signin.html')
