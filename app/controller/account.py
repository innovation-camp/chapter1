import hashlib

from flask import Blueprint, render_template, request, g, redirect, url_for

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


@bp.route('/api/check-email', methods=['POST'])
def check_email():
    email_receive = request.form.get('usermail')

    if not email_receive:
        return render_template('account/signup.html', res={
            "status_code": 400,
            "msg": "이메일을 입력해주세요"
        })

    if len(email_receive.split('@')) < 2:
        return render_template('account/signup.html', res={
            "status_code": 400,
            "msg": "올바른 이메일 형식이 아닙니다."
        })

    db = get_db()

    email = db.user.find_one({"email": email_receive})
    if email:
        return render_template('account/signup.html', res={
            "status_code": 409,
            "msg": "중복된 이메일입니다."
        })
    return redirect(url_for('account.signup'))





@bp.route('/api/signup', methods=['POST'])
def api_signup():
    email = request.form.get('usermail')
    password = request.form.get('userpw')
    password_check = request.form.get('userpwcheck')
    nickname = request.form.get('usernickname')

    if password != password_check:
        return render_template('account/signup.html', msg="비밀번호가 일치하지 않습니다.")

    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    db = get_db()
    db.user.insert_one({"email": email, "password": hashed_password, "nickname": nickname})

    return redirect(url_for('account.signin'))


@bp.route('/api/signin')
def api_signin():
    return render_template('account/signin.html')
