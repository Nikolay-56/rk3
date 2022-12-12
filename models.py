from app import db 

class Table(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    capital = db.Column(db.String)
    population = db.Column(db.Integer)
    language = db.Column(db.String)

    
