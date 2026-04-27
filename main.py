from flask import Flask, request, abort, jsonify
from config import get_admin_user, get_admin_password, get_secret_key
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = get_secret_key()
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == get_admin_user() and password == get_admin_password():
        return jsonify(access_token=create_access_token(identity="admin"))
    else:
        abort(401)

@app.route("/set_status", methods=["PATCH"])
@jwt_required()
def set_status():
    user_id = request.form["user_id"]
    set_ban = request.form["set_ban"] # banned?
    # ban user
    return "success"

@app.route("/", methods=["GET"])
def root():
    return "test"


app.run(port=5000)