from application import db

""" 
Create models for all the database tables to be used in the application
"""

# the publications model for the publications table in the database


class publications(db.Model):
    _id = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    doc_name = db.Column(db.String(150), nullable=False)
    date_added = db.Column(db.String(150), nullable=False)
    size = db.Column(db.String(150), nullable=False)
    downloads = db.Column(db.String(10))
    contents = db.Column(db.String(20000000), nullable=False)

    def __repr__(self):
        return f"publications('{self.doc_name}, {self.date_added}, {self.size}, {self.downloads}, {self.contents}')"


# the sectors data model to hold all the data for each particular sector


class Sector(db.Model):
    _id = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    npgei = db.Column(db.String(10))
    sector = db.Column(db.String(30))
    indicator = db.Column(db.String(90))
    source = db.Column(db.String(30))
    geo = db.Column(db.String(30))
    tier = db.Column(db.String(10))
    males_2013 = db.Column(db.String(10))
    females_2013 = db.Column(db.String(10))
    total_2013 = db.Column(db.String(10))
    males_2015 = db.Column(db.String(10))
    females_2015 = db.Column(db.String(10))
    total_2015 = db.Column(db.String(10))
    males_2017 = db.Column(db.String(10))
    females_2017 = db.Column(db.String(10))
    total_2017 = db.Column(db.String(10))
    males_2021 = db.Column(db.String(10))
    females_2021 = db.Column(db.String(10))
    total_2021 = db.Column(db.String(10))

    def __repr__(self):
        return f"Sector('{self._id},{self.npgei},{self.sector},{self.indicator},{self.source},{self.geo},{self.tier},{self.males_2013},{self.females_2013},{self.total_2013},{self.males_2015},{self.females_2015},{self.total_2015},{self.males_2017},{self.females_2017},{self.total_2017},{self.males_2021},{self.females_2021},{self.total_2021}')"


# the meta-data model to store all indicators' meta information


class Metadata(db.Model):
    indicator = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    definition = db.Column(db.String(2000))
    unit = db.Column(db.String(30))
    method = db.Column(db.String(500))
    compilation = db.Column(db.String(1000))
    source = db.Column(db.String(200))
    disaggregation = db.Column(db.String(50))
    accessibility = db.Column(db.String(50))
    periodicity = db.Column(db.String(50))
    comments = db.Column(db.String(90))

    def __repr__(self):
        return f"Sector('{self.indicator},{self.definition},{self.unit},{self.method},{self.compilation},{self.source},{self.disaggregation},{self.accessibility},{self.periodicity},{self.comments}')"

