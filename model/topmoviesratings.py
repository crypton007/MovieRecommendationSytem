from database import db, engine
from sqlalchemy import Table


moviesRatings = Table('topmoviesratings', db.metadata, autoload=True, autoload_with=engine)

class moviesRatingsModel(db.Model):
    __table__ = moviesRatings  
    __mapper_args__ =   {
                        'primary_key' :[moviesRatings.columns.movieid], 
                        }