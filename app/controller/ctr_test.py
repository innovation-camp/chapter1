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
def TestDBConncect():
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

# 새 글 등록하기
@bp.route('/posts', methods=["POST"])
def board_create():
    db = get_db()
    title_receive = request.form['title_give']
    description_receive = request.form['description_give']
    is_selling_receive = request.form['is_selling_give']
    condition_receive = request.form['condition_give']
    price_receive = request.form['price_give']
    location_receive = request.form['location_give']
    genre_receive = request.form['genre_give']
    contact_receive = request.form['contact_give']
    count = list(db.board.find({}, {'_id': False}))
    num = len(count) + 1
    doc = {
        'num': num,
        'title': title_receive,
        'description': description_receive,
        'is_selling': is_selling_receive,
        'condition' : condition_receive,
        'price': price_receive,
        'location' : location_receive,
        'genre' : genre_receive,
        'contact' : contact_receive,
        'is_soldout': 0,
        'writer': "",
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now()

    }
    db.board.insert_one(doc)
    return jsonify({'msg':'글이 성공적으로 작성되었습니다!'})