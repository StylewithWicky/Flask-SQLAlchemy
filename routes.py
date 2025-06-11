from flask import Blueprint,jsonify,request
from lib.service import create_user

bp= Blueprint('routes', __name__)
@bp.route('/create-user', methods=['POST'])
def handle_create_user():
    data = request.json
    user = create_user(data['username'], data['email'])
    return jsonify({"id": user.id})