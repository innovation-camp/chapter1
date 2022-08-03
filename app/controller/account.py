import os
import jwt
import hashlib
from datetime import datetime, timedelta

from bson import ObjectId
from flask import Blueprint, render_template, request, g, redirect, url_for, flash, make_response

from app.db import get_db
from app.decorators.login_required import login_required

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/')
@login_required
def account_test():
    return "hi"


@bp.route('/login-success')
@login_required
def login_success():
    return "로그인 성공~"


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


@bp.route('/api/signin', methods=['POST'])
def api_signin():
    email = request.form.get('usermail')
    password = request.form.get('userpw')
    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    db = get_db()
    user = db.user.find_one({'email': email})

    if not user:
        flash('존재하지 않는 회원입니다.')
        return redirect(url_for('account.signin'))

    if user['password'] != pw_hash:
        flash('비밀번호가 일치하지 않습니다.')
        return redirect(url_for('account.signin'))

    payload = {
        '_id': str(user['_id']),
        'exp': datetime.utcnow() + timedelta(hours=3)
    }

    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')

    response = make_response(redirect(url_for('account.login_success')))
    response.set_cookie(key='token', value=token)
    return response



@bp.before_app_request
def load_logged_in_user():
    token = request.cookies.get('token')

    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
        user_id = payload.get('_id')

        if not user_id:
            raise Exception('토큰 정보가 잘못되었습니다.')

        db = get_db()
        g.user = db.user.find_one({'_id': ObjectId(user_id)})

    except:
        flash("유효하지 않은 토큰입니다.")
        return redirect(url_for('account.signin'))

