from generic.model import BaseModel, db


class ProjectModel(BaseModel):
    __tablename__ = "projects"

    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    expirationDate = db.Column(db.Date, nullable=False)
