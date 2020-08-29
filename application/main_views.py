from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash,
    jsonify,
)
from application import app


@app.route("/")
def home():
    return render_template("./main_pages/home.html")


@app.route("/data")
def data():
    return render_template("./main_pages/data.html")
