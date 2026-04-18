from generic.model import BaseModel, db


class SaleModel(BaseModel):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=True)
    discount = db.Column(db.Float, nullable=False)

    product = db.relationship("ProductModel", back_populates="sales", lazy=True)
