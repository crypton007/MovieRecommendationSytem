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
    genres = db.relationship("Genre",secondary=MovieGenres, back_populates="movies")


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String())
    movies = db.relationship("moviesRatingsModel",secondary=MovieGenres, back_populates="genres")
    
    def __init__(self,id,genre):
        self.id = id
        self.genre = genre


        
# class MovieGenres(db.Model):
#     movieid = db.Column(db.Integer, db.ForeignKey('movies.movieid'), primary_key=True)
#     genreid = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)

#     movie = db.relationship("Movie", back_populates="genres")
#     genre = db.relationship("Genre", back_populates="movies")

#     def __init__(self, movieid, genreid):
#         self.movieid = movieid
#         self.genreid = genreid