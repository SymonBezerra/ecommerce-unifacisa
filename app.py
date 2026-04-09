import os

from flask import Flask, render_template
from flask_login import LoginManager

from generic.model import db
from users.model import UserModel


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return UserModel.get(user_id)


@app.route("/")
def home():
    return render_template("home.html")
