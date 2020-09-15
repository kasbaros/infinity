from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "11606633055e40cbe882f08f27fec5c2501f8978"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///genderstatsport.db"

db = SQLAlchemy(app)

from application import main_views

