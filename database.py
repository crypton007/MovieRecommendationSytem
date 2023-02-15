from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()
engine = create_engine('postgresql://postgres:root@localhost/moviedatabase')
db.metadata.bind = engine