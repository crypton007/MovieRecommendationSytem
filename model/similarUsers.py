from database import db

class SimilarUsers(db.Model):
    __tablename__ = 'similaruserids'
    userid = db.Column(db.Integer, primary_key=True)
    similaruserid_1 = db.Column(db.String())
    similaruserid_2 = db.Column(db.String())
    similaruserid_3 = db.Column(db.String())
    similaruserid_4 = db.Column(db.String())
    similaruserid_5 = db.Column(db.String())
    similaruserid_6 = db.Column(db.String())
    similaruserid_7 = db.Column(db.String())
    similaruserid_8 = db.Column(db.String())
    similaruserid_9 = db.Column(db.String())
    similaruserid_10 = db.Column(db.String())

    
    def __init__(self, userid, similaruserid_1, similaruserid_2, similaruserid_3, similaruserid_4, similaruserid_5, similaruserid_6, similaruserid_7, similaruserid_8, similaruserid_9, similaruserid_10):
        self.userid = userid
        self.similaruserid_1 = similaruserid_1
        self.similaruserid_2 = similaruserid_2
        self.similaruserid_3 = similaruserid_3
        self.similaruserid_4 = similaruserid_4
        self.similaruserid_5 = similaruserid_5
        self.similaruserid_6 = similaruserid_6
        self.similaruserid_7 = similaruserid_7
        self.similaruserid_8 = similaruserid_8
        self.similaruserid_9 = similaruserid_9
        self.similaruserid_10 = similaruserid_10