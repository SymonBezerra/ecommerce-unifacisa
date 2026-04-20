from flask import Blueprint, jsonify, render_template, request, redirect, url_for

from flask_login import login_required

from users.model import UserModel


users_bp = Blueprint(
    "users",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/users",
)


@users_bp.get("/")
@login_required
def list():
    users = UserModel.query.all()
    return render_template("users/list.html", users=users)


@users_bp.get("/create")
@login_required
def create():
    return redirect(url_for("login.register"))


@users_bp.route("/edit/<int:user_id>", methods=("GET", "PATCH"))
@login_required
def edit(user_id):
    user = UserModel.query.get_or_404(user_id)

    if request.method == "PATCH":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password != confirm_password:
            return jsonify({"error": "Passwords do not match"}), 400

        user.username = username
        if password:
            user.password = password

        user.save()

        return jsonify({"message": "User updated successfully"}), 200

    return render_template("users/edit.html", username=user.username, user_id=user.id)


@users_bp.delete("/delete/<int:user_id>")
@login_required
def delete(user_id):
    user = UserModel.query.get_or_404(user_id)
    user.delete()
    return jsonify({"message": "User deleted successfully"}), 200
