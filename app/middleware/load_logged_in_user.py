import os

import jwt
from bson import ObjectId
from flask import request, g, Blueprint

from app.db import get_db


bp = Blueprint('load_logged_in_user', __name__)

@bp.before_app_request
def load_logged_in_user():
    token = request.cookies.get('token')

    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
        user_id = payload.get('_id')

        if not user_id:
            raise Exception('토큰 정보가 잘못되었습니다.')

        db = get_db()
        g.user = db.user.find_one({'_id': ObjectId(user_id)})

    except:
        print("Error!")
