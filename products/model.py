from generic.model import BaseModel, db


class ProductModel(BaseModel):
    __tablename__ = "products"

    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
