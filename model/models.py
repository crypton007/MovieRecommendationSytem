from database import db,engine
from sqlalchemy import Table,Column

MovieGenres= Table('movie_genres', db.metadata,
                   Column('movieid',db.Integer, db.ForeignKey('topmovies.movieid')),
                   Column('genreid',db.Integer, db.ForeignKey('genre.id'))
                   )

moviesRatings = Table('topmovies', db.metadata, autoload=True, autoload_with=engine)

class moviesRatingsModel(db.Model):
    __table__ = moviesRatings  
    __mapper_args__ =   {
                        'primary_key' :[moviesRatings.columns.movieid], 
                        }
    genresrel = db.relationship("Genre",secondary=MovieGenres, back_populates="movies")


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String())
    movies = db.relationship("moviesRatingsModel",secondary=MovieGenres, back_populates="genresrel")
    
    def __init__(self,id,genre):
        self.id = id
        self.genre = genre


        
