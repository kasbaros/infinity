import os
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, template_folder="templates")
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)


from application import main_views

if __name__ == "__main__":
    manager.run()
