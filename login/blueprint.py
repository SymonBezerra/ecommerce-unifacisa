from flask import Blueprint, jsonify, render_template, request
from flask_login import login_required, login_user, logout_user

from users.model import UserModel


login_bp = Blueprint(
    "login",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/login",
)


# TODO: implement hashing for passwords
@login_bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        return render_template("login/index.html")
    elif request.method == "POST":
        data = request.get_json()
        user = UserModel.query.filter_by(username=data["username"]).first()
        if user and user.password == data["password"]:
            login_user(user)
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401


@login_bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "GET":
        return render_template("login/create.html")
    elif request.method == "POST":
        data = request.get_json()
        if data["password"] != data["confirmPassword"]:
            return jsonify({"error": "Passwords do not match"}), 400
        user = UserModel(username=data["username"], password=data["password"])
        user.save()
        return jsonify({"message": "User created successfully"}), 201


@login_required
@login_bp.post("/logout")
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200
