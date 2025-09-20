
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

#PythonAnywhere DB
host1 = "chonghe.mysql.pythonanywhere-services.com"
port1 = 3306
username1 = "chonghe"
database1 = "chonghe$default"
password1 = "0G3lCGnXD"
# app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username1}:{password1}@{host1}:{port1}/{database1}"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(50))

class Switch(db.Model):
    __tablename__ = "switch"
    id = db.Column(db.Integer, primary_key=True)
    switch = db.Column(db.Boolean)
    time = db.Column(db.String(12)) 

@app.route("/")
def home():
    return "Flask + MySQL is running! 🎉"

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    data = [{"id": u.id, "age": u.age, "name": u.name} for u in users]
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")


@app.route("/switch", methods=["GET"])
def get_switch():
    switches = Switch.query.all()
    data = [{"id": s.id, "switch": s.switch, "time": s.time} for s in switches]
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@app.route("/switch/latest", methods=["GET"])
def get_latest_switch():
    # 按时间降序排序（最新的在前），并取第一条记录
    latest_switch = Switch.query.order_by(Switch.time.desc()).first()
    
    if latest_switch:
        # 如果有记录，返回最新数据
        data = {
            "id": latest_switch.id,
            "switch": latest_switch.switch,
            "time": latest_switch.time
        }
        return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")
    else:
        # 如果没有记录，返回空数据和404状态码
        return Response(
            json.dumps({"error": "没有找到开关记录"}, ensure_ascii=False),
            mimetype="application/json",
            status=404
        )


def compare_time(t1, t2):
    return t1 > t2

if __name__ == "__main__":
    app.run(debug=True)
