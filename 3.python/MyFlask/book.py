from flask import Blueprint
bookbp = Blueprint('book', __name__)  # 必须写不一样的名字 不然重名报错

@bookbp.route('/')
def index():
    return 'book'
