from flask import Flask, request, abort, jsonify, redirect, url_for
from config import get_admin_user, get_admin_password, get_secret_key
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, verify_jwt_in_request
from db import set_is_banned
import random

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = get_secret_key()
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    add_claims = {"rnd_int": random.randint(1_000, 1_000_000)}
    if username == get_admin_user() and password == get_admin_password():
        return jsonify(access_token=create_access_token(identity="admin",
                                                        additional_claims=add_claims))
    else:
        abort(401)

@app.route("/set_status", methods=["PATCH"])
@jwt_required()
def set_status():
    user_id = request.form["user_id"]
    set_ban = request.form["set_ban"]
    try:
        result = set_is_banned(user_id, set_ban)
        return {"result": result}
    except Exception:
        return {"result": "False" }


@app.route("/", methods=["GET"])
def root():
    try:
        verify_jwt_in_request()
        return redirect(url_for("panel"))
    except Exception:
        return redirect(url_for("login"))


app.run(port=6000)