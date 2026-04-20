from flask import Blueprint, render_template, request
from flask_login import login_required

from sales.model import SaleModel


sales_bp = Blueprint(
    "sales",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/sales",
)


@sales_bp.get("/")
@login_required
def list():
    sales = SaleModel.query.all()
    return render_template("sales/list.html", sales=sales)


@sales_bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        data = request.get_json()
        description = data.get("description")
        product_id = data.get("sku")
        discount = data.get("discount")

        try:
            sale = SaleModel(
                description=description, product_id=product_id, discount=discount
            )
            sale.save()
            return {"message": "Sale created successfully"}, 201
        except Exception as e:
            return {"error": str(e)}, 400
    elif request.method == "GET":
        return render_template("sales/create.html")


@sales_bp.route("/edit/<int:sale_id>", methods=("GET", "PATCH"))
@login_required
def edit(sale_id):
    sale = SaleModel.query.get_or_404(sale_id)

    if request.method == "PATCH":
        data = request.get_json()
        sale.description = data.get("description", sale.description)
        sale.product_id = data.get("sku", sale.product_id)
        sale.discount = data.get("discount", sale.discount)

        try:
            sale.save()
            return {"message": "Sale updated successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 400
    elif request.method == "GET":
        return render_template("sales/edit.html", sale=sale)


@sales_bp.delete("/delete/<int:sale_id>")
@login_required
def delete(sale_id):
    sale = SaleModel.query.get_or_404(sale_id)

    try:
        sale.delete()
        return {"message": "Sale deleted successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
