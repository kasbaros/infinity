from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "11606633055e40cbe882f08f27fec5c2501f8978"
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:////static/data/database/genderstatsport.db"

"""POSTGRES = {
    "user": "postgres",
    "pw": "password",
    "db": "genderstatsport",
    "host": "localhost",
    "port": "5432",
}
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s"
    % POSTGRES
)"""

db = SQLAlchemy(app)

from application import main_views

