from database import db

class movies(db.Model):
    movieid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    genre = db.Column(db.String())
    
    def __init__(self,movieid,title,genre):
        self.movieid = movieid
        self.title = title
        self.genre = genre