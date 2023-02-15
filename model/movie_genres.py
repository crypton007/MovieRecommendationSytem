from database import db
from movies import movies

class MovieGenres(db.Model):
    movieid = db.Column(db.Integer, db.ForeignKey('movies.movieid'), primary_key=True)
    genreid = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)

    movie = db.relationship("Movie", back_populates="genres")
    genre = db.relationship("Genre", back_populates="movies")

    def __init__(self, movieid, genreid):
        self.movieid = movieid
        self.genreid = genreid

