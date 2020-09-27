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
    # form = ContactForm()
    # if form.validate_on_submit():
    #   return redirect(url_for("home"))
    return render_template("./main_pages/home.html")


@app.route("/accountability")
def accountability():
    fetch_all = Sector.query.filter(Sector.sector.match("accountability"))
    return render_template(
        "./main_pages/accountability.html", accountability_data=fetch_all
    )


@app.route("/agriculture")
def agriculture():
    fetch_all = Sector.query.filter(Sector.sector.match("agriculture"))
    return render_template("./main_pages/agriculture.html", agriculture_data=fetch_all)


@app.route("/education")
def education():
    fetch_all = Sector.query.filter(Sector.sector.match("education"))
    return render_template("./main_pages/education.html", education_data=fetch_all)


@app.route("/energy_and_mineral_development")
def energy_and_mineral_development():
    fetch_all = Sector.query.filter(
        Sector.sector.match("energy_and_mineral_development")
    )
    return render_template(
        "./main_pages/energy_and_mineral_development.html", energy_data=fetch_all
    )


@app.route("/health")
def health():
    fetch_all = Sector.query.filter(Sector.sector.match("health"))
    return render_template("./main_pages/health.html", health_data=fetch_all)


@app.route("/ict_and_national_guidance")
def ict_and_national_guidance():
    fetch_all = Sector.query.filter(Sector.sector.match("ict_and_national_guidance"))
    return render_template(
        "./main_pages/ict_and_national_guidance.html", ict_data=fetch_all
    )


@app.route("/justice_law_and_order")
def justice_law_and_order():
    fetch_all = Sector.query.filter(Sector.sector.match("justice,_law_and_order"))
    return render_template(
        "./main_pages/justice_law_and_order.html", justice_data=fetch_all
    )


@app.route("/lands_and_housing")
def lands_and_housing():
    fetch_all = Sector.query.filter(Sector.sector.match("lands_and_housing"))
    return render_template("./main_pages/lands_and_housing.html", lands_data=fetch_all)


@app.route("/public_sector_management")
def public_sector_management():
    fetch_all = Sector.query.filter(Sector.sector.match("public_sector_management"))
    return render_template(
        "./main_pages/public_sector_management.html", public_data=fetch_all
    )


@app.route("/science_technology_and_innovation")
def science_technology_and_innovation():
    fetch_all = Sector.query.filter(
        Sector.sector.match("science,_technology_and_innovation")
    )
    return render_template(
        "./main_pages/science_technology_and_innovation.html", tech_data=fetch_all
    )


@app.route("/social_development")
def social_development():
    fetch_all = Sector.query.filter(Sector.sector.match("social_development"))
    return render_template(
        "./main_pages/social_development.html", social_data=fetch_all
    )


@app.route("/water_and_environment")
def water_and_environment():
    fetch_all = Sector.query.filter(Sector.sector.match("water_and_environment"))
    return render_template(
        "./main_pages/water_and_environment.html", water_data=fetch_all
    )


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

