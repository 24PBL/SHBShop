from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from enum import Enum
import smtplib
from email.message import EmailMessage
import random
import threading
from sqlalchemy import desc
from werkzeug.utils import secure_filename
from uuid import uuid4
from werkzeug.security import generate_password_hash
from werkzeug.security import generate_password_hash, check_password_hash

# 에디터에서 에러 표시 나와도 무시하면 됩니다.
# 절대 경로 파악이 안 되는 것. 실행은 정상적으로 됩니다.
from models import Personal, Commercial, Auth4pjoin, Vaild4pjoin, Auth4cjoin, Vaild4cjoin, Auth4pfpw, Auth4cfpw, Vaild4pfpw, Vaild4cfpw, Commercialcert, Adminacc
from extensions import db
from utils import jwt_helper

auth_bp = Blueprint("auth", __name__)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

class UserType(Enum):
    PERSONAL = 1
    COMMERCIAL = 2
    ADMIN = 3

P_PROFILE_UPLOAD_FOLDER = "static/user/personal"
C_PROFILE_UPLOAD_FOLDER = "static/user/commercial"
LICENCE_UPLOAD_FOLDER = "static/licence"

def delete_auth_code_4_join(kind, email, authCode):
    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    try:
        if kind == UserType.PERSONAL.value:
            record = db.session.query(Auth4pjoin).filter_by(email=email, authCode=authCode).first()
        elif kind == UserType.COMMERCIAL.value:
            record = db.session.query(Auth4cjoin).filter_by(email=email, authCode=authCode).first()
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404
        
        if record:
            db.session.delete(record)
            db.session.commit()
    except Exception as e:
        print("삭제 실패:", e)

def delete_auth_code_4_fpw(kind, email, authCode):
    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    try:
        if kind == UserType.PERSONAL.value:
            record = db.session.query(Auth4pfpw).filter_by(email=email, authCode=authCode).first()
        elif kind == UserType.COMMERCIAL.value:
            record = db.session.query(Auth4cfpw).filter_by(email=email, authCode=authCode).first()
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404
        
        if record:
            db.session.delete(record)
            db.session.commit()
    except Exception as e:
        print("삭제 실패:", e)

def delete_all_auth_code_4_join(kind, email):
    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400
    
    try:
        if kind == UserType.PERSONAL.value:
            records = db.session.query(Auth4pjoin).filter_by(email=email).all()
        elif kind == UserType.COMMERCIAL.value:
            records = db.session.query(Auth4cjoin).filter_by(email=email).all()
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404
        
        for record in records:
            db.session.delete(record)

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print("삭제 실패:", e)

def delete_all_auth_code_4_vaild(kind, email):
    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    try:
        if kind == UserType.PERSONAL.value:
            records = db.session.query(Vaild4pjoin).filter_by(email=email).all()
        elif kind == UserType.COMMERCIAL.value:
            records = db.session.query(Vaild4cjoin).filter_by(email=email).all()
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404
        
        for record in records:
            db.session.delete(record)

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print("삭제 실패:", e)

def delete_all_auth_code_4_fpw(kind, email):
    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400
    
    try:
        if kind == UserType.PERSONAL.value:
            records = db.session.query(Auth4pfpw).filter_by(email=email).all()
        elif kind == UserType.COMMERCIAL.value:
            records = db.session.query(Auth4cfpw).filter_by(email=email).all()
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404
    
        for record in records:
            db.session.delete(record)

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print("삭제 실패:", e)

@auth_bp.route("/join/personal/check-email", methods=["POST"])
def check_personal_email():
    data = request.get_json()
    email = data.get("email")
    exPUser = db.session.query(Personal).filter_by(email=email).first()
    exCUser = db.session.query(Commercial).filter_by(email=email).first()
    reqCount = db.session.query(Auth4pjoin).filter_by(email=email).count()

    if not email:
        return jsonify({"message": "이메일이 제공되지 않았습니다."}), 400

    if exPUser:
        return jsonify({"message": "이미 가입된 회원입니다."}), 403
    elif exCUser:
        return jsonify({"message": "상업회원으로 가입되어 있습니다."}), 403
    elif (not exPUser) and (reqCount > 3) :
        return jsonify({"message": "인증 요청을 너무 많이 시도했습니다. 잠시 후에 시도해주세요."}), 429
    elif (not exPUser) and (reqCount <=3):
        code = random.randint(100000, 999999)

        new_auth4p = Auth4pjoin(email=email, authCode = code)

        db.session.add(new_auth4p)
        db.session.commit()

        try:
            msg = EmailMessage()
            msg["Subject"] = "헌책방 개인 회원가입 인증코드입니다."
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = email
            msg.set_content(f"인증코드는 {code}입니다.")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            
            timer = threading.Timer(300.0, delete_auth_code_4_join, args=[UserType.PERSONAL.value, email, code])  # 5분 = 300초
            timer.start()

            return jsonify({"message": f"{email}로 이메일 전송 성공!"}), 201
        except Exception as e:
            db.session.delete(new_auth4p)
            db.session.commit()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "알 수 없는 에러"}), 400
    
@auth_bp.route("/join/personal/check-auth-code", methods=["POST"])
def check_personal_auth_code():
    data = request.get_json()
    email = data.get("email")
    try:
        authCode = int(data.get("authCode"))
    except (TypeError, ValueError):
        return jsonify({"error": "잘못된 인증코드 형식입니다."}), 400
    
    pjoin = db.session.query(Auth4pjoin).filter_by(email=email).order_by(desc(Auth4pjoin.idx)).first()

    if not pjoin:
        return jsonify({"message": "해당 이메일의 인증 요청이 없습니다."}), 404

    if pjoin.authCode == authCode:
        delete_all_auth_code_4_join(UserType.PERSONAL.value, email)
        new_vaild4p = Vaild4pjoin(email=email, authCode=authCode)
        db.session.add(new_vaild4p)
        db.session.commit()
        return jsonify({"message": "이메일 인증 성공"}), 200
    else:
        return jsonify({"message": "인증번호가 올바르지 않습니다."}), 400
    
@auth_bp.route("/join/personal/fill-user-info", methods=["POST"])
def personal_signup():
    name = request.form.get("name")
    birth = request.form.get("birth")
    tel = request.form.get("tel")
    email = request.form.get("email")
    password = request.form.get("password")
    nickname = request.form.get("nickname")
    address = request.form.get("address")
    imgfile = request.files.get("imgfile")

    try:
        authCode = int(request.form.get("authCode"))
    except (TypeError, ValueError):
        return jsonify({"error": "잘못된 인증코드 형식입니다."}), 400

    if not all([name, birth, tel, email, password, nickname, address, authCode, imgfile]):
        return jsonify({"error": "모든 정보를 입력해주세요."}), 400
    
    hashed_pw = generate_password_hash(password)
    
    pvaild = db.session.query(Vaild4pjoin).filter_by(email=email).order_by(desc(Vaild4pjoin.idx)).first()

    if not pvaild:
        return jsonify({"message": "해당 이메일은 인증 과정을 거치지 않았습니다."}), 404

    if pvaild.authCode == authCode:
        delete_all_auth_code_4_vaild(UserType.PERSONAL.value, email)
        
        # 고유 파일명 생성
        filename = secure_filename(f"{uuid4().hex}_{imgfile.filename}")
        save_path = os.path.join(P_PROFILE_UPLOAD_FOLDER, filename)
        
        try:
            imgfile.save(save_path)
        except Exception as e:
            return jsonify({"error": f"파일 저장 실패: {str(e)}"}), 500

        profile_url = f"/{P_PROFILE_UPLOAD_FOLDER}/{filename}"

        region = address.split()[0] + "-" + address.split()[1]

        new_user = Personal(
            name=name,
            birth = birth,
            tel = tel,
            email=email,
            password=hashed_pw,
            nickname = nickname,
            address = address,
            region = region,
            img = profile_url
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "회원가입 완료"}), 201
    else:
        return jsonify({"message": "정상적이지 않은 회원가입 절차"}), 400

@auth_bp.route("/join/commercial/check-email", methods=["POST"])
def check_commercial_email():
    data = request.get_json()
    email = data.get("email")
    exPUser = db.session.query(Personal).filter_by(email=email).first()
    exCUser = db.session.query(Commercial).filter_by(email=email).first()
    reqCount = db.session.query(Auth4cjoin).filter_by(email=email).count()

    if not email:
        return jsonify({"message": "이메일이 제공되지 않았습니다."}), 400

    if exCUser:
        return jsonify({"message": "이미 가입된 회원입니다."}), 403
    elif exPUser:
        return jsonify({"message": "개인 회원으로 가입되어 있습니다."}), 403
    elif (not exCUser) and (reqCount > 3) :
        return jsonify({"message": "인증 요청을 너무 많이 시도했습니다. 잠시 후에 시도해주세요."}), 429
    elif (not exCUser) and (reqCount <=3):
        code = random.randint(100000, 999999)

        new_auth4c = Auth4cjoin(email=email, authCode=code)

        db.session.add(new_auth4c)
        db.session.commit()

        try:
            msg = EmailMessage()
            msg["Subject"] = "헌책방 회원가입 인증코드입니다."
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = email
            msg.set_content(f"인증코드는 {code}입니다.")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            
            timer = threading.Timer(300.0, delete_auth_code_4_join, args=[UserType.COMMERCIAL.value, email, code])  # 5분 = 300초
            timer.start()

            return jsonify({"message": f"{email}로 이메일 전송 성공!"}), 201
        except Exception as e:
            db.session.delete(new_auth4c)
            db.session.commit()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "알 수 없는 에러"}), 400

@auth_bp.route("/join/commercial/check-auth-code", methods=["POST"])
def check_commercial_auth_code():
    data = request.get_json()
    email = data.get("email")
    try:
        authCode = int(data.get("authCode"))
    except (TypeError, ValueError):
        return jsonify({"error": "잘못된 인증코드 형식입니다."}), 400
    
    cjoin = db.session.query(Auth4cjoin).filter_by(email=email).order_by(desc(Auth4cjoin.idx)).first()

    if not cjoin:
        return jsonify({"message": "해당 이메일의 인증 요청이 없습니다."}), 404

    if cjoin.authCode == authCode:
        delete_all_auth_code_4_join(UserType.COMMERCIAL.value, email)
        new_vaild4c = Vaild4cjoin(email=email, authCode=authCode)
        db.session.add(new_vaild4c)
        db.session.commit()
        return jsonify({"message": "이메일 인증 성공"}), 200
    else:
        return jsonify({"message": "인증번호가 올바르지 않습니다."}), 400
    
@auth_bp.route("/join/commercial/fill-user-info", methods=["POST"])
def commercial_signup():
    name = request.form.get("name")
    presidentName = request.form.get("presidentName")
    businessmanName = request.form.get("businessmanName")
    birth = request.form.get("birth")
    tel = request.form.get("tel")
    email = request.form.get("email")
    businessEmail = request.form.get("businessEmail")
    password = request.form.get("password")
    nickname = request.form.get("nickname")
    address = request.form.get("address")
    coNumber = request.form.get("coNumber")
    imgfile = request.files.get("imgfile")
    licence = request.files.get("licence")

    try:
        authCode = int(request.form.get("authCode"))
    except (TypeError, ValueError):
        return jsonify({"error": "잘못된 인증코드 형식입니다."}), 400

    if not all([name, presidentName, businessmanName, birth, tel, email, businessEmail, password, nickname, address, authCode, imgfile, licence, coNumber]):
        return jsonify({"error": "모든 정보를 입력해주세요."}), 400
    
    hashed_pw = generate_password_hash(password)
    
    cvaild = db.session.query(Vaild4cjoin).filter_by(email=email).order_by(desc(Vaild4cjoin.idx)).first()

    if not cvaild:
        return jsonify({"message": "해당 이메일은 인증 과정을 거치지 않았습니다."}), 404

    if cvaild.authCode == authCode:
        delete_all_auth_code_4_vaild(UserType.COMMERCIAL.value, email)
        
        # 고유 파일명 생성
        filename = secure_filename(f"{uuid4().hex}_{imgfile.filename}")
        save_path = os.path.join(C_PROFILE_UPLOAD_FOLDER, filename)
        
        try:
            imgfile.save(save_path)
        except Exception as e:
            return jsonify({"error": f"파일 저장 실패: {str(e)}"}), 500

        profile_url = f"/{C_PROFILE_UPLOAD_FOLDER}/{filename}"

        pdf_filename = secure_filename(f"{uuid4().hex}_{licence.filename}")
        pdf_save_path = os.path.join(LICENCE_UPLOAD_FOLDER, pdf_filename)

        try:
            licence.save(pdf_save_path)
        except Exception as e:
            return jsonify({"error": f"PDF 저장 실패: {str(e)}"}), 500

        pdf_url = f"/{LICENCE_UPLOAD_FOLDER}/{pdf_filename}"

        new_user = Commercial(
            name = name,
            presidentName = presidentName,
            businessmanName = businessmanName,
            birth = birth,
            tel = tel,
            email=email,
            businessEmail = businessEmail,
            password=hashed_pw,
            nickname = nickname,
            address = address,
            img=profile_url,
            licence=pdf_url,
            coNumber=coNumber
        )
        db.session.add(new_user)
        db.session.commit()

        cuser = db.session.query(Commercial).filter_by(email=email).first()

        new_certReq = Commercialcert(
            name=name,
            presidentName = presidentName,
            businessmanName = businessmanName,
            birth = birth,
            tel = tel,
            email=email,
            businessEmail = businessEmail,
            address = address,
            coNumber=coNumber,
            licence=pdf_url,
            cid=cuser.cid
        )

        db.session.add(new_certReq)
        db.session.commit()

        return jsonify({"message": "회원가입 완료"}), 201
    else:
        return jsonify({"message": "정상적이지 않은 회원가입 절차"}), 400
    
@auth_bp.route("/find-email", methods=["POST"])
def check_user_info():
    data = request.get_json()
    kind = data.get("kind")
    name = data.get("name")
    birth = data.get("birth")
    tel = data.get("tel")

    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    if kind == UserType.PERSONAL.value:
        exUser = db.session.query(Personal).filter_by(name=name, birth=birth, tel=tel).first()
    elif kind == UserType.COMMERCIAL.value:
        exUser = db.session.query(Commercial).filter_by(name=name, birth=birth, tel=tel).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404
    
    if exUser:
        email = exUser.email
        try:
            local, domain = email.split("@")

            visible_n = 3

            masked_local = local[:visible_n] + "*" * max(0, len(local) - visible_n)
            masked_domain = domain[:visible_n] + "*" * max(0, len(domain) - visible_n)

            masked_email = f"{masked_local}@{masked_domain}"

            return jsonify({
                "message": f"회원님의 이메일은 {masked_email}입니다."
            })
        except Exception as e:
            return jsonify({"error": f"이메일 처리 중 오류: {str(e)}"}), 500
    else:
        return jsonify({"message": "일치하는 사용자가 없습니다."}), 404

@auth_bp.route("/find-password/check-email", methods=["POST"])
def check_info_4_fpw():
    data = request.get_json()

    kind = data.get("kind")
    name = data.get("name")
    birth = data.get("birth")
    tel = data.get("tel")
    email = data.get("email")

    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    if kind == UserType.PERSONAL.value:
        exUser = db.session.query(Personal).filter_by(name=name, birth=birth, tel=tel, email = email).first()
        reqCount = db.session.query(Auth4pfpw).filter_by(email=email).count()
    elif kind == UserType.COMMERCIAL.value:
        exUser = db.session.query(Commercial).filter_by(name=name, birth=birth, tel=tel, email = email).first()
        reqCount = db.session.query(Auth4cfpw).filter_by(email=email).count()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404

    if (not exUser):
        return jsonify({"message": "일치하는 사용자가 없습니다."}), 404
    elif (exUser) and (reqCount > 3):
        return jsonify({"message": "인증 요청을 너무 많이 시도했습니다. 잠시 후에 시도해주세요."}), 429
    elif (exUser) and (reqCount <= 3):
        code = random.randint(100000, 999999)

        if kind == UserType.PERSONAL.value:
            new_auth4fpw = Auth4pfpw(email=email, authCode = code, name=name, birth=birth, tel=tel)
        elif kind == UserType.COMMERCIAL.value:
            new_auth4fpw = Auth4cfpw(email=email, authCode = code, name=name, birth=birth, tel=tel)
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404

        db.session.add(new_auth4fpw)
        db.session.commit()

        try:
            msg = EmailMessage()
            msg["Subject"] = "헌책방 비밀번호 변경 인증코드입니다."
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = email
            msg.set_content(f"인증코드는 {code}입니다.")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            
            timer = threading.Timer(300.0, delete_auth_code_4_fpw, args=[email, code])  # 5분 = 300초
            timer.start()

            return jsonify({"message": f"{email}로 이메일 전송 성공!"}), 201
        except Exception as e:
            db.session.delete(new_auth4fpw)
            db.session.commit()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "알 수 없는 에러"}), 400
    
@auth_bp.route("/find-password/check-auth-code", methods=["POST"])
def check_auth_code_4_fpw():
    data = request.get_json()
    kind = data.get("kind")
    email = data.get("email")

    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    try:
        authCode = int(data.get("authCode"))
    except (TypeError, ValueError):
        return jsonify({"error": "잘못된 인증코드 형식입니다."}), 400
    
    if kind == UserType.PERSONAL.value:
        find = db.session.query(Auth4pfpw).filter_by(email=email).order_by(desc(Auth4pfpw.idx)).first()
    elif kind == UserType.COMMERCIAL.value:
        find = db.session.query(Auth4cfpw).filter_by(email=email).order_by(desc(Auth4cfpw.idx)).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404

    if not find:
        return jsonify({"message": "비밀번호 변경 절차가 올바르지 않음"}), 404

    if find.authCode == authCode:
        if kind == UserType.PERSONAL.value:
            delete_all_auth_code_4_fpw(UserType.PERSONAL.value, email)
            new_vaild = Vaild4pfpw(email=email, authCode=authCode)
        elif kind == UserType.COMMERCIAL.value:
            delete_all_auth_code_4_fpw(UserType.COMMERCIAL.value, email)
            new_vaild = Vaild4cfpw(email=email, authCode=authCode)
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404
        
        db.session.add(new_vaild)
        db.session.commit()
        return jsonify({"message": "이메일 인증 성공"}), 200
    else:
        return jsonify({"message": "인증번호가 올바르지 않습니다."}), 400
    
@auth_bp.route("/find-password/modify-pw", methods=["PUT"])
def change_pw():
    data = request.get_json()

    kind = data.get("kind")
    email = data.get("email")
    pw = data.get("pw")

    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    if kind == UserType.PERSONAL.value:
        exUser = db.session.query(Personal).filter_by(email = email).first()
        vaild = db.session.query(Vaild4pfpw).filter_by(email=email).order_by(desc(Vaild4pfpw.idx)).first()
    elif kind == UserType.COMMERCIAL.value:
        exUser = db.session.query(Commercial).filter_by(email = email).first()
        vaild = db.session.query(Vaild4cfpw).filter_by(email=email).order_by(desc(Vaild4cfpw.idx)).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404

    try:
        authCode = int(data.get("authCode"))
    except (TypeError, ValueError):
        return jsonify({"error": "잘못된 인증코드 형식입니다."}), 400

    if not vaild:
        return jsonify({"message": "해당 이메일은 인증 과정을 거치지 않았습니다."}), 404

    if vaild.authCode == authCode:
        if kind == UserType.PERSONAL.value:
            delete_all_auth_code_4_vaild(UserType.PERSONAL.value, email)
        elif kind == UserType.COMMERCIAL.value:
            delete_all_auth_code_4_vaild(UserType.COMMERCIAL.value, email)
        else:
            return jsonify({"error": "잘못된 유저 유형"}), 404
        
        hashed_pw = generate_password_hash(pw)
        exUser.password = hashed_pw
        db.session.commit()

        return jsonify({"message": "비밀번호 변경 완료"}), 200
    else:
        return jsonify({"message": "정상적이지 않은 비밀번호 변경 절차"}), 400

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    kind = data.get("kind")

    try:
        kind = int(kind)
    except (TypeError, ValueError):
        return jsonify({"error": "유효하지 않은 유형 값입니다."}), 400

    if kind == UserType.PERSONAL.value:
        user = db.session.query(Personal).filter_by(email=email).first()
    elif kind == UserType.COMMERCIAL.value:
        user = db.session.query(Commercial).filter_by(email=email).first()
    elif kind == UserType.ADMIN.value:
        user = db.session.query(Adminacc).filter_by(acc=email).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404

    if not user:
        return jsonify({"error": "존재하지 않는 계정입니다."}), 404
    
    if (kind == UserType.PERSONAL.value) or (kind == UserType.COMMERCIAL.value):
        if not check_password_hash(user.password, password):
            return jsonify({"error": "비밀번호가 일치하지 않습니다."}), 400
    elif kind == UserType.ADMIN.value:
        if user.password != password:
            return jsonify({"error": "비밀번호가 일치하지 않습니다."}), 400
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404

    if kind == UserType.PERSONAL.value:
        user_id = user.pid
    elif kind == UserType.COMMERCIAL.value:
        user_id = user.cid
    elif kind == UserType.ADMIN.value:
        user_id = user.aid

    token = jwt_helper.generate_jwt(user_id, kind)

    # 로그인은 jwt만 보냄, 이후에는 jwt로 바로 메인화면 api 호출
    return jsonify({"message": "로그인 성공", "token": token}), 200