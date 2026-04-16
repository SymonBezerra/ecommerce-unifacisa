from flask import Blueprint, render_template, request
from flask_login import login_required


from products.model import ProjectModel


products_bp = Blueprint(
    "products",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/products",
)


@login_required
@products_bp.get("/")
def list():
    return render_template("products/list.html")


@login_required
@products_bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "GET":
        return render_template("products/create.html")
    elif request.method == "POST":
        data = request.get_json()
        project = ProjectModel(
            name=data["name"],
            description=data["description"],
            type=data["type"],
            price=data["price"],
            expirationDate=data["expirationDate"],
        )
        try:
            project.save()
            return {"message": "Project created successfully!"}, 201
        except Exception as e:
            return {"error": str(e)}, 400
