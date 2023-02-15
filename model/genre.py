from database import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String())
    
    def __init__(self,id,genre):
        self.id = id
        self.genre = genre