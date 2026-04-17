from datetime import datetime

from flask import Blueprint, render_template, request
from flask_login import login_required


from products.model import ProductModel


products_bp = Blueprint(
    "products",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/products",
)


@products_bp.get("/")
@login_required
def list():
    products = ProductModel.query.all()
    return render_template("products/list.html", products=products)


@products_bp.get("/<int:product_id>")
@login_required
def index(product_id):
    product = ProductModel.query.get_or_404(product_id)
    return render_template("products/index.html", product=product)


@products_bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "GET":
        return render_template("products/create.html")
    elif request.method == "POST":
        data = request.get_json()
        product = ProductModel(
            name=data["name"],
            description=data["description"],
            type=data["type"],
            price=data["price"],
            expirationDate=datetime.strptime(data["expirationDate"], "%d/%m/%Y").date(),
        )
        try:
            product.save()
            return {"message": "Product created successfully!"}, 201
        except Exception as e:
            return {"error": str(e)}, 400
