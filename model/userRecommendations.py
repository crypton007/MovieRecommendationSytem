from database import db

class UserRecommendations(db.Model):
    __tablename__ = 'userrecommendations'
    userid = db.Column(db.Integer, primary_key=True)
    recommendation_1 = db.Column(db.String())
    recommendation_2 = db.Column(db.String())
    recommendation_3 = db.Column(db.String())
    recommendation_4 = db.Column(db.String())
    recommendation_5 = db.Column(db.String())
    recommendation_6 = db.Column(db.String())
    recommendation_7 = db.Column(db.String())
    recommendation_8 = db.Column(db.String())
    recommendation_9 = db.Column(db.String())
    recommendation_10 = db.Column(db.String())

    
    def __init__(self, userid, recommendation_1, recommendation_2, recommendation_3, recommendation_4, recommendation_5, recommendation_6, recommendation_7, recommendation_8, recommendation_9, recommendation_10):
        self.userid = userid
        self.recommendation_1 = recommendation_1
        self.recommendation_2 = recommendation_2
        self.recommendation_3 = recommendation_3
        self.recommendation_4 = recommendation_4
        self.recommendation_5 = recommendation_5
        self.recommendation_6 = recommendation_6
        self.recommendation_7 = recommendation_7
        self.recommendation_8 = recommendation_8
        self.recommendation_9 = recommendation_9
        self.recommendation_10 = recommendation_10