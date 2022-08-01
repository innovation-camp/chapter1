import os

from flask import Flask
from dotenv import load_dotenv
from app.db import get_db
from pymongo.errors import OperationFailure

load_dotenv(verbose=True)


def create_app(test_config=None):
    # create and configure the app
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

    # a simple page that says hello
    @app.route('/hello')
    def hello():

        return '''
                <div align="center">
                    <h1 align="center">Hello, World! 👋</h1>
                </div>
                '''

    @app.route('/db-connect-test')
    def db_connect_test():

        try:
            db = get_db()
            doc = {
                'name': 'hi'
            }
            db.hello.insert_one(doc)

        except OperationFailure:
            return '''
                    <div align="center">
                        <h1>DB connection <b style="color:red">Failed 👻</b></h1>
                        <p style="font-size:1.5rem"> Please check <b>.env</b> file! </p>
                    </div>
                    '''

        return '''
                <div align="center">
                    <h1>DB connection <b style="color:green">Succeeded! 🥳</b></h1>'
                </div>
                '''

    return app