from flask import Blueprint, request, jsonify, current_app
import os
from dotenv import load_dotenv
from sqlalchemy import desc
from werkzeug.utils import secure_filename
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

# 에디터에서 에러 표시 나와도 무시하면 됩니다.
# 절대 경로 파악이 안 되는 것. 실행은 정상적으로 됩니다.
from models import Personal, Commercial, Commercialcert, Adminacc, Shop, Pbooktrade, Cbooktrade, Sbooktrade
from extensions import db

test_bp = Blueprint("test", __name__)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

P_PROFILE_UPLOAD_FOLDER = "static/user/personal"
C_PROFILE_UPLOAD_FOLDER = "static/user/commercial"
S_IMAGE_UPLOAD_FOLDER = "static/shop"
LICENCE_UPLOAD_FOLDER = "static/licence"

@test_bp.route("/add-personal", methods=["POST"])
def add_personal():
    name = request.form.get("name")
    birth = request.form.get("birth")
    tel = request.form.get("tel")
    email = request.form.get("email")
    password = request.form.get("password")
    nickname = request.form.get("nickname")
    address = request.form.get("address")
    imgfile = request.files.get("imgfile")

    filename = secure_filename(f"{uuid4().hex}_{imgfile.filename}")
    save_path = os.path.join(P_PROFILE_UPLOAD_FOLDER, filename)
        
    try:
        imgfile.save(save_path)
    except Exception as e:
        return jsonify({"error": f"파일 저장 실패: {str(e)}"}), 500

    profile_url = f"/{P_PROFILE_UPLOAD_FOLDER}/{filename}"

    region = address.split()[0] + "-" + address.split()[1]
    hashed_pw = generate_password_hash(password)

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

@test_bp.route("/add-commercial", methods=["POST"])
def add_commercial():
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
    
    hashed_pw = generate_password_hash(password)
    
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

    region = address.split()[0] + "-" + address.split()[1]

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
        coNumber=coNumber,
        region=region
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

@test_bp.route("/add-admin", methods=["POST"])
def add_admin():
    data = request.get_json()
    name = data.get("name")
    acc = data.get("acc")
    password = data.get("password")
    
    hashed_pw = generate_password_hash(password)

    new_user = Adminacc(
        name = name,
        acc = acc,
        password=hashed_pw
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "회원가입 완료"}), 201


@test_bp.route("/add-shop", methods=["POST"])
def add_shop():
    cid = request.form.get("cid")
    cid = int(cid)
    presidentName = request.form.get("presidentName")
    businessmanName = request.form.get("businessmanName")
    shopName = request.form.get("shopName")
    shoptel = request.form.get("shoptel")
    businessEmail = request.form.get("businessEmail")
    address = request.form.get("address")
    region = address.split()[0] + "-" + address.split()[1]
    shopOpen = request.form.get("open")
    shopClose = request.form.get("close")
    holiday = request.form.get("holiday")
    etc = request.form.get("etc")
    imgfile1 = request.files.get("imgfile1")
    imgfile2 = request.files.get("imgfile2")
    imgfile3 = request.files.get("imgfile3")
    
    filename1 = secure_filename(f"{uuid4().hex}_{imgfile1.filename}")
    save_path1 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename1)

    filename2 = secure_filename(f"{uuid4().hex}_{imgfile2.filename}")
    save_path2 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename2)

    filename3 = secure_filename(f"{uuid4().hex}_{imgfile3.filename}")
    save_path3 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename3)
        
    try:
        imgfile1.save(save_path1)
        imgfile2.save(save_path2)
        imgfile3.save(save_path3)
    except Exception as e:
        return jsonify({"error": f"파일 저장 실패: {str(e)}"}), 500

    shopimg_url1 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename1}"
    shopimg_url2 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename2}"
    shopimg_url3 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename3}"   

    new_shop = Shop(
        cid = cid,
        presidentName = presidentName,
        businessmanName = businessmanName,
        shopName = shopName,
        shoptel = shoptel,
        businessEmail = businessEmail,
        address = address,
        region=region,
        open=shopOpen,
        close=shopClose,
        holiday=holiday,
        etc=etc,
        shopimg1=shopimg_url1,
        shopimg2=shopimg_url2,
        shopimg3=shopimg_url3
    )
    db.session.add(new_shop)
    db.session.commit()

    return jsonify({"message": "가게추가 완료"}), 201

@test_bp.route("/add-pbook", methods=["POST"])
def add_pbook():
    pid = request.form.get("pid")
    pid = int(pid)
    title = request.form.get("title")
    author = request.form.get("author")
    publish = request.form.get("publish")
    isbn = request.form.get("isbn")
    price = request.form.get("price")
    price = int(price)
    detail = request.form.get("detail")
    region = request.form.get("region")
    imgfile1 = request.files.get("imgfile1")
    imgfile2 = request.files.get("imgfile2")
    imgfile3 = request.files.get("imgfile3")
    
    filename1 = secure_filename(f"{uuid4().hex}_{imgfile1.filename}")
    save_path1 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename1)

    filename2 = secure_filename(f"{uuid4().hex}_{imgfile2.filename}")
    save_path2 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename2)

    filename3 = secure_filename(f"{uuid4().hex}_{imgfile3.filename}")
    save_path3 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename3)
        
    try:
        imgfile1.save(save_path1)
        imgfile2.save(save_path2)
        imgfile3.save(save_path3)
    except Exception as e:
        return jsonify({"error": f"파일 저장 실패: {str(e)}"}), 500

    img_url1 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename1}"
    img_url2 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename2}"
    img_url3 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename3}"   

    new_pbook = Pbooktrade(
        pid = pid,
        title = title,
        author = author,
        publish = publish,
        isbn = isbn,
        price = price,
        detail = detail,
        region = region,
        img1 = img_url1,
        img2 = img_url2,
        img3 = img_url3
    )
    db.session.add(new_pbook)
    db.session.commit()

    return jsonify({"message": "책 추가 완료"}), 201

@test_bp.route("/add-cbook", methods=["POST"])
def add_cbook():
    cid = request.form.get("cid")
    cid = int(cid)
    title = request.form.get("title")
    author = request.form.get("author")
    publish = request.form.get("publish")
    isbn = request.form.get("isbn")
    price = request.form.get("price")
    price = int(price)
    detail = request.form.get("detail")
    region = request.form.get("region")
    imgfile1 = request.files.get("imgfile1")
    imgfile2 = request.files.get("imgfile2")
    imgfile3 = request.files.get("imgfile3")
    
    filename1 = secure_filename(f"{uuid4().hex}_{imgfile1.filename}")
    save_path1 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename1)

    filename2 = secure_filename(f"{uuid4().hex}_{imgfile2.filename}")
    save_path2 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename2)

    filename3 = secure_filename(f"{uuid4().hex}_{imgfile3.filename}")
    save_path3 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename3)
        
    try:
        imgfile1.save(save_path1)
        imgfile2.save(save_path2)
        imgfile3.save(save_path3)
    except Exception as e:
        return jsonify({"error": f"파일 저장 실패: {str(e)}"}), 500

    img_url1 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename1}"
    img_url2 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename2}"
    img_url3 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename3}"   

    new_cbook = Cbooktrade(
        cid = cid,
        title = title,
        author = author,
        publish = publish,
        isbn = isbn,
        price = price,
        detail = detail,
        region = region,
        img1 = img_url1,
        img2 = img_url2,
        img3 = img_url3
    )
    db.session.add(new_cbook)
    db.session.commit()

    return jsonify({"message": "책 추가 완료"}), 201

@test_bp.route("/add-sbook", methods=["POST"])
def add_sbook():
    sid = request.form.get("sid")
    sid = int(sid)
    title = request.form.get("title")
    author = request.form.get("author")
    publish = request.form.get("publish")
    isbn = request.form.get("isbn")
    price = request.form.get("price")
    price = int(price)
    detail = request.form.get("detail")
    region = request.form.get("region")
    imgfile1 = request.files.get("imgfile1")
    imgfile2 = request.files.get("imgfile2")
    imgfile3 = request.files.get("imgfile3")
    
    filename1 = secure_filename(f"{uuid4().hex}_{imgfile1.filename}")
    save_path1 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename1)

    filename2 = secure_filename(f"{uuid4().hex}_{imgfile2.filename}")
    save_path2 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename2)

    filename3 = secure_filename(f"{uuid4().hex}_{imgfile3.filename}")
    save_path3 = os.path.join(S_IMAGE_UPLOAD_FOLDER, filename3)
        
    try:
        imgfile1.save(save_path1)
        imgfile2.save(save_path2)
        imgfile3.save(save_path3)
    except Exception as e:
        return jsonify({"error": f"파일 저장 실패: {str(e)}"}), 500

    img_url1 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename1}"
    img_url2 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename2}"
    img_url3 = f"/{S_IMAGE_UPLOAD_FOLDER}/{filename3}"   

    new_sbook = Sbooktrade(
        sid = sid,
        title = title,
        author = author,
        publish = publish,
        isbn = isbn,
        price = price,
        detail = detail,
        region = region,
        img1 = img_url1,
        img2 = img_url2,
        img3 = img_url3
    )
    db.session.add(new_sbook)
    db.session.commit()

    return jsonify({"message": "책 추가 완료"}), 201
