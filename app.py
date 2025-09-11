# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

# # ⚠️ 修改下面的连接信息为你的远程 MySQL
# username = "testusersqlpub"
# password = "iDNOaRaK1SOUaDFS"
# host = "mysql5.sqlpub.com"
# port = 3310  # 默认是 3306
# database = "sqlpubchonghe"

# app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)
# # 定义 User 模型（对应 MySQL 的 user 表）
# class User(db.Model):
#     __tablename__ = "user"   # 表名要和 MySQL 的表一致
#     id = db.Column(db.Integer, primary_key=True)
#     age = db.Column(db.Integer)
#     name = db.Column(db.String(50))

# def home():
#     return "Flask + MySQL is running! 🎉"

# # 查询所有用户
# @app.route("/users", methods=["GET"])
# @app.route("/users", methods=["GET"])
# def get_users():
#     users = User.query.all()
#     return jsonify([{"id": u.id, "age": u.age, "name": u.name} for u in users])


# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 尝试保持中文
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 远程 MySQL 配置
username = "testusersqlpub"
password = "iDNOaRaK1SOUaDFS"
host = "mysql5.sqlpub.com"
port = 3310
database = "sqlpubchonghe"

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(50))

@app.route("/")
def home():
    return "Flask + MySQL is running! 🎉"

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    data = [{"id": u.id, "age": u.age, "name": u.name} for u in users]
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)
