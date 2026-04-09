from flask import Blueprint, render_template


login_bp = Blueprint(
    "login",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/login",
)


@login_bp.route("/", methods=("GET",))
def index():
    return render_template("login/index.html")
