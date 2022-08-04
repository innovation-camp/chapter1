from flask import render_template, Blueprint, jsonify, request
from app.db import get_db

# parameter (블루프린터 별칭, 모듈명, axis url)
bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('')
def main():
    return render_template('base.html')


@bp.route('/welcome')
def welcome():
    return render_template('welcome.html')


# todo : is_delete 적용, is_selling 정상값으로 변경
@bp.route('/api/getList', methods=['POST'])
def get_list():
    global data
    db = get_db()
    request_data = dict(request.json);
    print(request_data)
    if request_data.get('category') is not None:
        data = list(db.board.find(
            {"category": request_data.get('category'), "is_selling": request_data.get('is_selling'),
             }, {"_id": False}))
    else:
        data = list(db.board.find(
            {"is_selling": "0",
             }, {"_id": False}))
    print(data)
    result = jsonify(data)
    return result
