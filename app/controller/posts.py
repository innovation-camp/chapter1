import datetime
from xmlrpc.client import boolean
from app.db import get_db
from jinja2 import Template
from flask import Blueprint, render_template, jsonify, request, g

# parameter (블루프린터 별칭, 모듈명, axis url)
from app.decorators.login_required import login_required

bp = Blueprint('post', __name__, url_prefix='/post')


# 글 작성 페이지
@bp.route("/")
@login_required
def create():
    return render_template("post/create.html")


# 인덱스 페이지
@bp.route("/index")
def board_index():
    return render_template("post/index.html")


# 새 글 등록하기
@bp.route('/', methods=["POST"])
@login_required
def board_create():
    db = get_db()
    title_receive = request.form['title_give']
    img_receive = request.form['img_give']
    description_receive = request.form['description_give']
    is_selling_receive = request.form['is_selling_give']
    condition_receive = request.form['condition_give']
    price_receive = request.form['price_give']
    location_receive = request.form['location_give']
    genre_receive = request.form['genre_give']
    contact_receive = request.form['contact_give']

    count = list(db.board.find({}, {'_id': False}))
    num = len(count) + 1
    
    selling = True if is_selling_receive=="1" else False
        
    doc = {
        'num': num,
        'title': title_receive,
        'img': img_receive,
        'description': description_receive,
        'is_selling': selling,
        'condition': condition_receive,
        'price': price_receive,
        'location': location_receive,
        'genre': genre_receive,
        'contact': contact_receive,
        'is_soldout': False,
        'is_deleted': False,
        'writer': g.user,
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now()
    }
    db.board.insert_one(doc)
    print("is_selling 값 알려죠", doc)

    return jsonify({'msg': '글이 성공적으로 작성되었습니다!'})


# 글 상세 보기
@bp.route("/<int:num>", methods=['GET'])
@login_required
def board_detail(num):
    db = get_db()
    post = db.board.find_one({'num': num}, {'_id': False})
    print(post)

    post = db.board.find_one({'num': num}, {'_id': False})
    writer = post.get('writer')

    is_owner = False

    if writer.get('_id') == g.user.get('_id'):
        is_owner = True

    template = Template("{{ date.strftime('%Y-%m-%d %H:%M:%S') }}")
    formated_date = template.render(date=post['created_at'])

    if post['is_deleted'] == True:
        return render_template('error.html')
    else:
        return render_template('post/detail.html',
                               post=post, board_id=int(num),
                               formated_date=formated_date, is_owner=is_owner)


# 글 수정하는 폼으로 이동
@bp.route('/<int:num>/edit', methods=['GET'])
@login_required
def board_edit(num):
    db = get_db()

    post = db.board.find_one({'num': num}, {'_id': False})
    writer = post.get('writer')

    # 본인 게시물이 아닌 경우 detail page로 redirect 하여 접근 제어
    if writer.get('_id') != g.user.get('_id'):
        return render_template('post/detail.html', post=post)
    return render_template('post/edit.html', post=post)


# 글 수정하기
@bp.route("/<int:num>", methods=['PATCH'])
@login_required
def board_update(num):
    db = get_db()

    title_receive = request.form['title_give']
    description_receive = request.form['description_give']
    is_selling_receive = request.form['is_selling_give']
    condition_receive = request.form['condition_give']
    price_receive = request.form['price_give']
    location_receive = request.form['location_give']
    genre_receive = request.form['genre_give']
    contact_receive = request.form['contact_give']
    updated_at = datetime.datetime.now()

    selling = True if is_selling_receive=="1" else False

    db.board.update_one({'num': int(num)}, {'$set': {'title': title_receive,
                                                     'description': description_receive,
                                                     'is_selling': selling,
                                                     'condition': condition_receive,
                                                     'price': price_receive,
                                                     'location': location_receive,
                                                     'genre': genre_receive,
                                                     'contact': contact_receive,
                                                     'is_soldout': False,
                                                     'updated_at': updated_at}})
    return jsonify({'msg': '수정 완료!'})


# 글 삭제하기
@bp.route("/<int:num>/delete", methods=['PATCH', 'GET'])
@login_required
def board_delete(num):
    db = get_db()

    post = db.board.find_one({'num': num}, {'_id': False})
    writer = post.get('writer')

    # 본인 게시물이 아닌 경우 detail page로 redirect 하여 접근 제어
    if writer.get('_id') != g.user.get('_id'):
        return render_template('post/detail.html', post=post)

    num_receive = request.form['num_give']
    is_delete = request.form['is_delete_give']
    db.board.update_one({'num': int(num_receive)}, {'$set': {'is_deleted': boolean(is_delete)}})
    return jsonify({'msg': '삭제 완료!'})
