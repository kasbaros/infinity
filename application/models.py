from application import db

""" 
Create models for all the database tables to be used in the application
"""

# the publications model for the publications table in the database

# drugs taken model
class publications(db.Model):
    _id = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    doc_name = db.Column(db.String(150), nullable=False)
    date_added = db.Column(db.String(150), nullable=False)
    size = db.Column(db.String(150), nullable=False)
    downloads = db.Column(db.String(10), nullable=False)
    contents = db.Column(db.String(20000000), nullable=False)

    def __repr__(self):
        return f"publications('{self.doc_name}, {self.date_added}, {self.size}, {self.downloads}, {self.contents}')"
