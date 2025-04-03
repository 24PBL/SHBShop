from flask import Blueprint, jsonify
from utils.jwt_helper import token_required

start_bp = Blueprint("start", __name__)

@start_bp.route("/", methods=["GET"])
@token_required
def check_user(decoded_user_id, user_type):
    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type
    })