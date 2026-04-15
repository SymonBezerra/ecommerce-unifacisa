from flask_login import UserMixin

from generic.model import BaseModel, db


class UserModel(BaseModel, UserMixin):
    __tablename__ = "users"

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
