import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate


# from sqlalchemy import create_engine

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "11606633055e40cbe882f08f27fec5c2501f8978"
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from application import main_views

