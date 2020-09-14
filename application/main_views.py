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
from .models import *
from .forms import ContactForm


@app.route("/", methods=("GET", "POST"))
def home():
    files = publications.query.all()
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("./main_pages/home.html", form=form)


@app.route("/accountability")
def accountability():
    return render_template("./main_pages/accountability.html")


@app.route("/agriculture")
def agriculture():
    return render_template("./main_pages/agriculture.html")


@app.route("/education")
def education():
    return render_template("./main_pages/education.html")


@app.route("/energy_and_mineral_development")
def energy_and_mineral_development():
    return render_template("./main_pages/energy_and_mineral_development.html")


@app.route("/health")
def health():
    return render_template("./main_pages/health.html")


@app.route("/ict_and_national_guidance")
def ict_and_national_guidance():
    return render_template("./main_pages/ict_and_national_guidance.html")


@app.route("/justice_law_and_order")
def justice_law_and_order():
    return render_template("./main_pages/justice_law_and_order.html")


@app.route("/lands_and_housing")
def lands_and_housing():
    return render_template("./main_pages/lands_and_housing.html")


@app.route("/public_sector_management")
def public_sector_management():
    return render_template("./main_pages/public_sector_management.html")


@app.route("/science_technology_and_innovation")
def science_technology_and_innovation():
    return render_template("./main_pages/science_technology_and_innovation.html")


@app.route("/social_development")
def social_development():
    return render_template("./main_pages/social_development.html")


@app.route("/water_and_environment")
def water_and_environment():
    return render_template("./main_pages/water_and_environment.html")


""" The maps routes here """


@app.route("/edu_map")
def edu_map():
    return render_template("./maps/education_map.html")

