from flask import Blueprint, request, jsonify
from enum import Enum
from sqlalchemy import desc, or_
from sqlalchemy.orm import joinedload
from utils.jwt_helper import token_required

from models import Personal, Commercial, Pbooktrade, Sbooktrade, Cbooktrade, Shop, Favorite4p, Favorite4c
from extensions import db

home_bp = Blueprint("home", __name__)

class UserType(Enum):
    PERSONAL = 1
    COMMERCIAL = 2
    ADMIN = 3

@home_bp.route("/<int:userId>", methods=["GET"])
@token_required
def show_user_home(decoded_user_id, user_type, userId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    if user_type == UserType.PERSONAL.value:
        userInfo = db.session.query(Personal).filter_by(pid=decoded_user_id).first()
    elif user_type == UserType.COMMERCIAL.value:
        userInfo = db.session.query(Commercial).filter_by(cid=decoded_user_id).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404
    
    pbook_results = (
        db.session.query(Pbooktrade, Personal.nickname)
        .join(Personal, Pbooktrade.pid == Personal.pid)
        .filter(Pbooktrade.region == userInfo.region)
        .order_by(Pbooktrade.createAt.desc())
        .limit(5)
        .all()
    )

    cbook_results = (
        db.session.query(Cbooktrade, Commercial.nickname)
        .join(Commercial, Cbooktrade.cid == Commercial.cid)
        .filter(Cbooktrade.region == userInfo.region)
        .order_by(Cbooktrade.createAt.desc())
        .limit(5)
        .all()
    )

    combined_list = []

    for book, nickname in pbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.PERSONAL.value
        })

    for book, nickname in cbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.COMMERCIAL.value
        })

    sorted_books = sorted(combined_list, key=lambda x: x["createAt"], reverse=True)

    for book in sorted_books:
        book["createAt"] = book["createAt"].isoformat()

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type,
        "region": userInfo.region,
        "bookList": sorted_books
    }), 200

@home_bp.route("/<int:userId>/<int:pfinidx>/<int:cfinidx>", methods=["GET"])
@token_required
def show_user_home_more(decoded_user_id, user_type, userId, pfinidx, cfinidx):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    if user_type == UserType.PERSONAL.value:
        userInfo = db.session.query(Personal).filter_by(pid=decoded_user_id).first()
    elif user_type == UserType.COMMERCIAL.value:
        userInfo = db.session.query(Commercial).filter_by(cid=decoded_user_id).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404
    
    pbook_results = (
        db.session.query(Pbooktrade, Personal.nickname)
        .join(Personal, Pbooktrade.pid == Personal.pid)
        .filter(
            Pbooktrade.region == userInfo.region,
            Pbooktrade.bid < pfinidx
        )
        .order_by(Pbooktrade.createAt.desc())
        .limit(5)
        .all()
    )

    cbook_results = (
        db.session.query(Cbooktrade, Commercial.nickname)
        .join(Commercial, Cbooktrade.cid == Commercial.cid)
        .filter(
            Cbooktrade.region == userInfo.region,
            Cbooktrade.bid < cfinidx
        )
        .order_by(Cbooktrade.createAt.desc())
        .limit(5)
        .all()
    )

    combined_list = []

    for book, nickname in pbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.PERSONAL.value
        })

    for book, nickname in cbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.COMMERCIAL.value
        })

    sorted_books = sorted(combined_list, key=lambda x: x["createAt"], reverse=True)

    for book in sorted_books:
        book["createAt"] = book["createAt"].isoformat()

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type,
        "region": userInfo.region,
        "bookList": sorted_books
    }), 200

@home_bp.route("/<int:userId>/search-book", methods=["GET"])
@token_required
def search_book(decoded_user_id, user_type, userId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    # const encoded = encodeURIComponent(keyword); 프론트에서 쿼리값 인코딩 해주세요.
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "검색어가 제공되지 않았습니다."}), 400

    keyword_pattern = f"%{keyword}%"

    pbook_results = (
        db.session.query(Pbooktrade, Personal.nickname)
        .join(Personal, Pbooktrade.pid == Personal.pid)
        .filter(
            or_(
                Pbooktrade.title.ilike(keyword_pattern),
                Pbooktrade.author.ilike(keyword_pattern),
                Pbooktrade.publish.ilike(keyword_pattern),
            )
        )
        .order_by(desc(Pbooktrade.createAt))
        .limit(3)
        .all()
    )

    cbook_results = (
        db.session.query(Cbooktrade, Commercial.nickname)
        .join(Commercial, Cbooktrade.cid == Commercial.cid)
        .filter(
            or_(
                Cbooktrade.title.ilike(keyword_pattern),
                Cbooktrade.author.ilike(keyword_pattern),
                Cbooktrade.publish.ilike(keyword_pattern),
            )
        )
        .order_by(desc(Cbooktrade.createAt))
        .limit(3)
        .all()
    )

    sbook_results = (
        db.session.query(Sbooktrade, Shop.shopName)
        .join(Shop, Sbooktrade.sid == Shop.sid)
        .filter(
            or_(
                Sbooktrade.title.ilike(keyword_pattern),
                Sbooktrade.author.ilike(keyword_pattern),
                Sbooktrade.publish.ilike(keyword_pattern)
            )
        )
        .order_by(desc(Sbooktrade.createAt))
        .limit(6)
        .all()
    )

    combined_list = []

    for book, nickname in pbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "publish": book.publish,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.PERSONAL.value
        })

    for book, nickname in cbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "publish": book.publish,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.COMMERCIAL.value
        })
    
    sbook_list = [{
        "bid": book.bid,
        "title": book.title,
        "author": book.author,
        "publish": book.publish,
        "price": book.price,
        "region": book.region,
        "shopName": shopName,
        "createAt": book.createAt
    } for book, shopName in sbook_results]

    sorted_books = sorted(combined_list, key=lambda x: x["createAt"], reverse=True)

    for book in sorted_books:
        book["createAt"] = book["createAt"].isoformat()

    if not sorted_books and not sbook_list:
        return jsonify({"message": "검색 결과가 없습니다.", "bookList": []}), 200

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type,
        "bookList": sorted_books,
        "sbookList": sbook_list
    }), 200

@home_bp.route("/<int:userId>/search-book/more-book/<int:pfinidx>/<int:cfinidx>", methods=["GET"])
@token_required
def search_more_book(decoded_user_id, user_type, userId, pfinidx, cfinidx):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    # const encoded = encodeURIComponent(keyword); 프론트에서 쿼리값 인코딩 해주세요.
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "검색어가 제공되지 않았습니다."}), 400

    keyword_pattern = f"%{keyword}%"

    pbook_results = (
        db.session.query(Pbooktrade, Personal.nickname)
        .join(Personal, Pbooktrade.pid == Personal.pid)
        .filter(
            Pbooktrade.bid < pfinidx,
            or_(
                Pbooktrade.title.ilike(keyword_pattern),
                Pbooktrade.author.ilike(keyword_pattern),
                Pbooktrade.publish.ilike(keyword_pattern),
            )
        )
        .order_by(desc(Pbooktrade.createAt))
        .limit(5)
        .all()
    )

    cbook_results = (
        db.session.query(Cbooktrade, Commercial.nickname)
        .join(Commercial, Cbooktrade.cid == Commercial.cid)
        .filter(
            Cbooktrade.bid < cfinidx,
            or_(
                Cbooktrade.title.ilike(keyword_pattern),
                Cbooktrade.author.ilike(keyword_pattern),
                Cbooktrade.publish.ilike(keyword_pattern),
            )
        )
        .order_by(desc(Cbooktrade.createAt))
        .limit(5)
        .all()
    )
    combined_list = []

    for book, nickname in pbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "publish": book.publish,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.PERSONAL.value
        })

    for book, nickname in cbook_results:
        combined_list.append({
            "bid": book.bid,
            "title": book.title,
            "author": book.author,
            "publish": book.publish,
            "price": book.price,
            "region": book.region,
            "nickname": nickname,
            "createAt": book.createAt,
            "userType": UserType.COMMERCIAL.value
        })
    
    sorted_books = sorted(combined_list, key=lambda x: x["createAt"], reverse=True)

    for book in sorted_books:
        book["createAt"] = book["createAt"].isoformat()

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type,
        "bookList": sorted_books,
    }), 200

@home_bp.route("/<int:userId>/search-book/more-sbook/<int:sfinidx>", methods=["GET"])
@token_required
def search_more_sbook(decoded_user_id, user_type, userId, sfinidx):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    # const encoded = encodeURIComponent(keyword); 프론트에서 쿼리값 인코딩 해주세요.
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "검색어가 제공되지 않았습니다."}), 400

    keyword_pattern = f"%{keyword}%"

    sbook_results = (
        db.session.query(Sbooktrade, Shop.shopName)
        .join(Shop, Sbooktrade.sid == Shop.sid)
        .filter(
            Sbooktrade.bid < sfinidx,
            or_(
                Sbooktrade.title.ilike(keyword_pattern),
                Sbooktrade.author.ilike(keyword_pattern),
                Sbooktrade.publish.ilike(keyword_pattern)
            )
        )
        .order_by(desc(Sbooktrade.createAt))
        .limit(10)
        .all()
    )
    
    sbook_list = [{
        "bid": book.bid,
        "title": book.title,
        "author": book.author,
        "publish": book.publish,
        "price": book.price,
        "region": book.region,
        "shopName": shopName,
        "createAt": book.createAt.isoformat()
    } for book, shopName in sbook_results]

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type,
        "sbookList": sbook_list
    }), 200

@home_bp.route("/<int:userId>/shop-mode/main", methods=["GET"])
@token_required
def get_shop_main(decoded_user_id, user_type, userId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    if user_type == UserType.PERSONAL.value:
        userInfo = db.session.query(Personal).filter_by(pid=decoded_user_id).first()

        favorite_results = (
            db.session.query(Favorite4p, Shop)
            .filter_by(pid=decoded_user_id)
            .join(Shop, Favorite4p.sid == Shop.sid)
            .order_by(Favorite4p.sid.desc())
            .all()
        )
    elif user_type == UserType.COMMERCIAL.value:
        userInfo = db.session.query(Commercial).filter_by(cid=decoded_user_id).first()

        favorite_results = (
            db.session.query(Favorite4c, Shop)
            .filter_by(cid=decoded_user_id)
            .join(Shop, Favorite4c.sid == Shop.sid)
            .order_by(Favorite4c.sid.desc())
            .all()
        )
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404
    
    favorite_list = [
        {
            "sid": shop.sid,
            "shopName": shop.shopName,
            "address": shop.address,
            "region": shop.region,
            "shoptel": shop.shoptel,
            "shopimg1": shop.shopimg1,
            "holiday": shop.holiday,
            "open": shop.open,
            "close": shop.close,
            "createAt": shop.createAt.isoformat()
        } for _, shop in favorite_results
    ]

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type,
        "favorite_list": favorite_list
    }), 200

@home_bp.route("/<int:userId>/shop-mode/search-shop", methods=["GET"])
@token_required
def search_shop(decoded_user_id, user_type, userId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    # const encoded = encodeURIComponent(keyword); 프론트에서 쿼리값 인코딩 해주세요.
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "검색어가 제공되지 않았습니다."}), 400

    keyword_pattern = f"%{keyword}%"

    shop_results = (
        db.session.query(Shop)
        .filter(
            or_(
                Shop.shopName.ilike(keyword_pattern),
                Shop.address.ilike(keyword_pattern)
            )
        )
        .order_by(desc(Shop.sid))
        .all()
    )

    shop_list = [{
        "sid": shop.sid,
        "shopName": shop.shopName,
        "shoptel": shop.shoptel,
        "region": shop.region,
        "shopimg": shop.shopimg1,
        "createAt": shop.createAt.isoformat()
    } for shop in shop_results]

    if not shop_list:
        return jsonify({"message": "검색 결과가 없습니다.", "shopList": []}), 200

    return jsonify({
        "decoded_user_id": decoded_user_id,
        "user_type": user_type,
        "shopList": shop_list
    }), 200

@home_bp.route("/<int:userId>/shop-mode/<int:shopId>/add-shop", methods=["POST"])
@token_required
def add_favorite_shop(decoded_user_id, user_type, userId, shopId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    sInfo = db.session.query(Shop).filter_by(sid=shopId).first()

    if not sInfo:
        return jsonify({"error": "일치하는 매장이 없습니다."}), 404
    
    if user_type == UserType.PERSONAL.value:
        pInfo = db.session.query(Personal).filter_by(pid=decoded_user_id).first()
        exFav = db.session.query(Favorite4p).filter_by(pid=decoded_user_id, sid=shopId).first()

        if not pInfo:
            return jsonify({"error": "일치하는 회원이 없습니다."}), 404
        
        if exFav:
            return jsonify({"message": "이미 즐겨찾기에 추가된 매장입니다."}), 409
        
        new_favorite4p = Favorite4p(pid=decoded_user_id, sid = shopId)

        db.session.add(new_favorite4p)
        db.session.commit()
        return jsonify({"message": "즐겨찾기 추가 성공", "decoded_user_id": decoded_user_id, "user_type": user_type,}), 201
    elif user_type == UserType.COMMERCIAL.value:
        cInfo = db.session.query(Commercial).filter_by(cid=decoded_user_id).first()
        exFav = db.session.query(Favorite4c).filter_by(cid=decoded_user_id, sid=shopId).first()

        if not cInfo:
            return jsonify({"error": "일치하는 회원이 없습니다."}), 404

        if exFav:
            return jsonify({"message": "이미 즐겨찾기에 추가된 매장입니다."}), 409
        
        new_favorite4c = Favorite4c(cid=decoded_user_id, sid = shopId)

        db.session.add(new_favorite4c)
        db.session.commit()
        return jsonify({"message": "즐겨찾기 추가 성공", "decoded_user_id": decoded_user_id, "user_type": user_type,}), 201
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404
    
@home_bp.route("/<int:userId>/shop-mode/<int:shopId>/delete-shop", methods=["DELETE"])
@token_required
def delete_favorite_shop(decoded_user_id, user_type, userId, shopId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    sInfo = db.session.query(Shop).filter_by(sid=shopId).first()

    if not sInfo:
        return jsonify({"error": "일치하는 매장이 없습니다."}), 404
    
    if user_type == UserType.PERSONAL.value:
        userInfo = db.session.query(Personal).filter_by(pid=decoded_user_id).first()
        exFav = db.session.query(Favorite4p).filter_by(pid=decoded_user_id, sid=shopId).first()
        
    elif user_type == UserType.COMMERCIAL.value:
        userInfo = db.session.query(Commercial).filter_by(cid=decoded_user_id).first()
        exFav = db.session.query(Favorite4c).filter_by(cid=decoded_user_id, sid=shopId).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404
    
    if not userInfo:
        return jsonify({"error": "일치하는 회원이 없습니다."}), 404
    
    if not exFav:
        return jsonify({"message": "즐겨찾기에 존재하지 않는 매장입니다."}), 404
    
    db.session.delete(exFav)
    db.session.commit()
    return jsonify({"message": "즐겨찾기 삭제 성공", "decoded_user_id": decoded_user_id, "user_type": user_type,}), 200

@home_bp.route("/<int:userId>/my-page", methods=["GET"])
@token_required
def get_my_page(decoded_user_id, user_type, userId):
    if str(decoded_user_id) != str(userId):
        return jsonify({"error": "권한이 없습니다."}), 403
    
    if user_type == UserType.PERSONAL.value:
        userData = db.session.query(Personal).filter_by(pid=decoded_user_id).first()
    elif user_type == UserType.COMMERCIAL.value:
        userData = db.session.query(Commercial).filter_by(cid=decoded_user_id).first()
    else:
        return jsonify({"error": "잘못된 유저 유형"}), 404

    if not userData:
        return jsonify({"error": "일치하는 회원이 없습니다."}), 404
    
    userInfo = {
        "name": userData.name,
        "nickname": userData.nickname,
        "email": userData.email,
        "region": userData.region,
        "profile": userData.img
    }

    return jsonify({"decoded_user_id": decoded_user_id, "user_type": user_type, "user_info": userInfo}), 200