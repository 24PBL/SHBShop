from controllers import blueprints
from controllers import *
from flask import Flask, request, jsonify
import config
# 에디터 오류 표시 무시하셔도 됩니다. 정상 실행됩니다.
from models import *
from extensions import db
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

for bp, prefix in blueprints:
    if prefix:
        app.register_blueprint(bp, url_prefix=prefix)
    else:
        app.register_blueprint(bp)

app.config.from_object(config.Config)

db.init_app(app)

# 디버그모드 자동 활성화 (실행은 - python app.py)
# flask run 하면 활성화 안 됨.
if __name__ == '__main__':
    app.run(debug=True)