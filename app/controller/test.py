from flask import Blueprint
from app.db import get_db
from pymongo.errors import OperationFailure

# parameter (블루프린터 별칭, 모듈명, axis url)
bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/')
def main():
    return '''
            <div align="center">
                <h1 align="center">Hello, World! 👋</h1>
            </div>
            '''


@bp.route('/check_db_connect')
def test_db_connect():
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
