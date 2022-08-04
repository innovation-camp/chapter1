from functools import wraps
from flask import g, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.get('user'):
            return redirect(url_for('account.signin'))
        return f(*args, **kwargs)
    return decorated_function
