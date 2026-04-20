import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_login import LoginManager, login_required

from sales.blueprint import sales_bp
from generic.model import db
from login.blueprint import login_bp
from products.blueprint import products_bp
from users.blueprint import users_bp
from users.model import UserModel


load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.register_blueprint(login_bp)
app.register_blueprint(products_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(users_bp)

with app.app_context():
    db.create_all()

login_manager.login_view = "login.index"


@login_manager.user_loader
def load_user(user_id):
    return UserModel.get(user_id)


@app.route("/")
@login_required
def home():
    return render_template("home.html")
