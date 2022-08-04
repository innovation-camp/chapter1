from flask import render_template, Blueprint, jsonify, request
from app.db import get_db

# parameter (블루프린터 별칭, 모듈명, axis url)
bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/list')
def main():
    return render_template('mainpage.html')


@bp.route('/')
def welcome():
    return render_template('welcome.html')


# todo : is_delete 적용, is_selling 정상값으로 변경
@bp.route('/api/getList', methods=['POST'])
def get_list():
    global data
    db = get_db()
    request_data = dict(request.json);
    if request_data.get('genre') is not None:
        data = list(db.board.find(
            {"genre": request_data.get('genre'), "is_selling": request_data.get('is_selling'),
             "is_deleted":False}, {"_id": False,"writer":False}).sort("created_at",-1))
    else:
        data = list(db.board.find(
            {"is_selling": request_data.get('is_selling'),
             "is_deleted":False}, {"_id": False,"writer":False}).sort("created_at",-1))
    result = jsonify(data)
    return result
