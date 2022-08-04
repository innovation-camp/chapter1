import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv(verbose=True)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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

    # 이곳에 컨트롤러 모듈관리를 해주세요
    from .controller import test
    app.register_blueprint(test.bp)
    from .controller import home
    app.register_blueprint(home.bp)


    app.debug = True
    return app
