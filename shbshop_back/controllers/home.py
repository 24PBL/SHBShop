from flask import Blueprint, jsonify
from utils.jwt_helper import token_required

home_bp = Blueprint("home", __name__)

@home_bp.route("/<int:userId>", methods=["GET"])
@token_required
# 임시로 로그인 확인을 위해 토큰 해독 정보만 보냄. 릴리즈 2에서는 해당 유저 메인화면 구성을 위한 정보까지 보낼 예정
def show_user_home(decoded_user_id, user_type, userId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type
    })