from flask import Blueprint, render_template, request
from flask_login import login_required


projects_bp = Blueprint(
    "projects",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/projects",
)


@login_required
@projects_bp.get("/")
def list():
    return render_template("projects/list.html")


@login_required
@projects_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("projects/create.html")
