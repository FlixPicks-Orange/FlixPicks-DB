from datetime import datetime
from config import db, ma

# User Model
class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    role = db.Column(db.String(32), default="Standard")
    registration_date = db.Column(db.DateTime,  default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    limit_subscriptions = db.Column(db.Boolean, default=True)
    survey_check = db.Column(db.Boolean, default=False)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schmea = UserSchema()
users_schema = UserSchema(many=True)


# Watch History Model
class WatchHistory(db.Model):
    __tablename__ = "WatchHistory"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    watched = db.Column(db.DateTime, default=datetime.utcnow)
    
class WatchHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WatchHistory
        load_instance = True
        sqla_session = db.session

WatchHistory_schema = WatchHistorySchema()
WatchHistorys_schema = WatchHistorySchema(many=True)


# Subscriptions Model
class Subscription(db.Model):
    __tablename__ = "Subscriptions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    provider_id = db.Column(db.Integer)
    
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription
        load_instance = True
        sqla_session = db.session

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)


# Recommendations Model
class Recommendations(db.Model):
    __tablename__ = "Recommendations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    recommended = db.Column(db.DateTime, default=datetime.utcnow)

class RecommendationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recommendations
        load_instance = True
        sqla_session = db.session

Recommendations_schema = RecommendationsSchema()
Recommendationss_schema = RecommendationsSchema(many=True)