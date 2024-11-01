from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello/', methods=['GET'])
def hello_world():
    return 'hello world'