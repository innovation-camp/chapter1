from flask import Blueprint, render_template

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/signup')
def signup():
    return render_template('account/signup.html')


@bp.route('/signin')
def signin():
    return render_template('account/signin.html')













