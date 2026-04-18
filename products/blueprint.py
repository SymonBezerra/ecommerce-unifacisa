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
            expiration_date=datetime.strptime(
                data["expirationDate"], "%d/%m/%Y"
            ).date(),
        )
        try:
            product.save()
            return {"message": "Product created successfully!"}, 201
        except Exception as e:
            return {"error": str(e)}, 400


@products_bp.route("/edit/<int:product_id>", methods=("GET", "PATCH"))
@login_required
def edit(product_id):
    product = ProductModel.query.get_or_404(product_id)
    if request.method == "GET":
        return render_template(
            "products/edit.html",
            product=product,
            expiration_date=product.expiration_date.strftime("%d/%m/%Y"),
        )
    elif request.method == "PATCH":
        data = request.get_json()
        product.name = data["name"]
        product.description = data["description"]
        product.type = data["type"]
        product.price = data["price"]
        product.expiration_dsate = datetime.strptime(
            data["expirationDate"], "%d/%m/%Y"
        ).date()
        try:
            product.save()
            return {"message": "Product updated successfully!"}, 200
        except Exception as e:
            return {"error": str(e)}, 400


@products_bp.delete("/delete/<int:product_id>")
@login_required
def delete(product_id):
    product = ProductModel.query.get_or_404(product_id)
    try:
        product.delete()
        return {"message": "Product deleted successfully!"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
