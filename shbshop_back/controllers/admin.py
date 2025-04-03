from flask import Blueprint, jsonify, request
from enum import Enum
from sqlalchemy import desc
from utils.jwt_helper import token_required

from models import Commercial, Commercialcert
from extensions import db

admin_bp = Blueprint("admin", __name__)

class UserType(Enum):
    PERSONAL = 1
    COMMERCIAL = 2
    ADMIN = 3

class State(Enum):
    REVIEW = 1
    ACCEPT = 2
    REJECT = 3

@admin_bp.route("/check-licence", methods=["GET"])
@token_required
def check_licence_list(decoded_user_id, user_type):
    if user_type != UserType.ADMIN.value:
        return jsonify({"error": "관리자만 접근 가능"}), 403
    
    licenceList = db.session.query(Commercialcert).order_by(desc(Commercialcert.createAt)).all()

    licenceList_serialized = [
        {
            "idx": cert.idx,
            "cid": cert.cid,
            "name": cert.name,
            "presidentName": cert.presidentName,
            "businessmanName": cert.businessmanName,
            "birth": cert.birth,
            "tel": cert.tel,
            "email": cert.email,
            "businessEmail": cert.businessEmail,
            "address": cert.address,
            "coNumber": cert.coNumber,
            "licence": cert.licence,
            "reason": cert.reason,
            "state": cert.state,
            "createAt": cert.createAt.isoformat()
        }
        for cert in licenceList
    ]
    return jsonify({"message": "리스트 응답 성공", "licenceList": licenceList_serialized}), 200

@admin_bp.route("/check-licence/<int:licenceId>", methods=["GET"])
@token_required
def check_licence_info(decoded_user_id, user_type, licenceId):
    if user_type != UserType.ADMIN.value:
        return jsonify({"error": "관리자만 접근 가능"}), 403
    
    licenceInfo = db.session.query(Commercialcert).filter_by(idx=licenceId).first()

    licenceInfo_serialized = \
    {
        "idx": licenceInfo.idx,
        "cid": licenceInfo.cid,
        "name": licenceInfo.name,
        "presidentName": licenceInfo.presidentName,
        "businessmanName": licenceInfo.businessmanName,
        "birth": licenceInfo.birth,
        "tel": licenceInfo.tel,
        "email": licenceInfo.email,
        "businessEmail": licenceInfo.businessEmail,
        "address": licenceInfo.address,
        "coNumber": licenceInfo.coNumber,
        "licence": licenceInfo.licence,
        "reason": licenceInfo.reason,
        "state": licenceInfo.state,
        "createAt": licenceInfo.createAt.isoformat()
    }
    return jsonify({"message": "승인 요청 정보 응답 성공", "licenceInfo": licenceInfo_serialized}), 200

@admin_bp.route("/check-licence/<int:licenceId>/review", methods=["PUT"])
@token_required
def review_licence(decoded_user_id, user_type, licenceId):
    if user_type != UserType.ADMIN.value:
        return jsonify({"error": "관리자만 접근 가능"}), 403

    data = request.get_json()

    decision = data.get("decision")
    reason = data.get("reason")

    try:
        decision = int(decision)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 결정 값입니다."}), 400
    
    licenceInfo = db.session.query(Commercialcert).filter_by(idx=licenceId).first()
    if not licenceInfo:
        return jsonify({"error": "해당 인증 요청을 찾을 수 없습니다."}), 404
    coUser = db.session.query(Commercial).filter_by(cid = licenceInfo.cid).first()
    if not coUser:
        return jsonify({"error": "해당 상업회원 정보를 찾을 수 없습니다."}), 404


    if decision == State.ACCEPT.value:
        coUser.state = 2
        licenceInfo.state = 2
    elif decision == State.REJECT.value:
        coUser.state = 3
        licenceInfo.state = 3
    else:
        return jsonify({"error": "유효하지 않은 결정"}), 404
    
    coUser.reason = reason
    licenceInfo.reason = reason

    db.session.commit()

    licenceList = db.session.query(Commercialcert).order_by(desc(Commercialcert.createAt)).all()

    licenceList_serialized = [
        {
            "idx": cert.idx,
            "cid": cert.cid,
            "name": cert.name,
            "presidentName": cert.presidentName,
            "businessmanName": cert.businessmanName,
            "birth": cert.birth,
            "tel": cert.tel,
            "email": cert.email,
            "businessEmail": cert.businessEmail,
            "address": cert.address,
            "coNumber": cert.coNumber,
            "licence": cert.licence,
            "reason": cert.reason,
            "state": cert.state,
            "createAt": cert.createAt.isoformat()
        }
        for cert in licenceList
    ]
    return jsonify({"message": "인증 요청 응답 성공", "licenceList": licenceList_serialized}), 200