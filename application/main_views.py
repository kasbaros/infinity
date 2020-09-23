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
    fetch_all = Sector.query.filter(Sector.sector == "health")
    """h_13m = Sector.query.filter(Sector.sector == health2013 
    h_13f = Sector.query.filter(Sector.sector == health2013 fe
    h_13t = Sector.query.filter(Sector.sector == health2013 
    h_14m = Sector.query.filter(Sector.sector == health2014 
    h_14f = Sector.query.filter(Sector.sector == health2014 fe
    h_14t = Sector.query.filter(Sector.sector == health2014 
    h_15m = Sector.query.filter(Sector.sector == health2015 
    h_15f = Sector.query.filter(Sector.sector == health2015 fe
    h_15t = Sector.query.filter(Sector.sector == health2015 
    h_16m = Sector.query.filter(Sector.sector == health2016 
    h_16f = Sector.query.filter(Sector.sector == health2016 fe
    h_16t = Sector.query.filter(Sector.sector == health2016 
    h_17m = Sector.query.filter(Sector.sector == health2017 
    h_17f = Sector.query.filter(Sector.sector == health2017 fe
    h_17t = Sector.query.filter(Sector.sector == health2017 
    h_21m = Sector.query.filter(Sector.sector == health2021
    h_21f = Sector.query.filter(Sector.sector == health2021
    h_21t = Sector.query.filter(Sector.sector == health2021"""
    return render_template(
        "./main_pages/health.html",
        health_data=fetch_all,
        # h_13m=h_13m,
        # h_13f=h_13f,
        # h_13t=h_13t,
        # h_14m=h_14m,
        # h_14f=h_14f,
        # h_14t=h_14t,
        # h_15m=h_15m,
        # h_15f=h_15f,
        # h_15t=h_15t,
        # h_16m=h_16m,
        # h_16f=h_16f,
        # h_16t=h_16t,
        # h_17m=h_17m,
        # h_17f=h_17f,
        # h_17t=h_17t,
        # h_21m=h_21m,
        # h_21f=h_21f,
        # h_21t=h_21t,
    )


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


""" Gender activities, Publications and Gallery routes """


@app.route("/gender_act")
def gender_acts():
    return render_template("./main_pages/gender_acts.html")


@app.route("/gallery")
def gallery():
    return render_template("./main_pages/gallery.html")


@app.route("/publication")
def publication():
    files = Publications.query.all()
    return render_template("./main_pages/publications.html", pubs=files)


""" The maps routes here """


@app.route("/edu_map")
def edu_map():
    return render_template("./maps/education_map.html")

