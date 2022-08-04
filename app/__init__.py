import os
from flask import Flask
from dotenv import load_dotenv

from app.db import get_db
from app.middleware.load_logged_in_user import load_logged_in_user

load_dotenv(verbose=True)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .middleware import load_logged_in_user
    app.register_blueprint(load_logged_in_user.bp)

    # 이곳에 컨트롤러 모듈관리를 해주세요
    from .controller import test
    app.register_blueprint(test.bp)

    from .controller import home
    app.register_blueprint(home.bp)

    from .controller import posts
    app.register_blueprint(posts.bp)

    from .controller import account
    app.register_blueprint(account.bp)

    app.debug = True
    return app
