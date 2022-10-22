from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.dialects.postgresql import JSON
# from flask_login import UserMixin
from app.config import SECRET_KEY
from app import db
import datetime


class User(db.Model):
    __tablename__ = 'user'  # Explicit is better than implicit.

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)  # Lenny
    last_name = db.Column(db.String(50), nullable=False)  # Ng'ang'a
    phone1 = db.Column(db.Text, nullable=False)  # Phone number
    # Optional further verification
    email = db.Column(db.String(100), nullable=True)
    pword = db.Column(db.String(256), nullable=False)  # Owner-pword
    # A user must change their passwords to be verified.
    is_verified = db.Column(db.Integer, nullable=False, default=0)
    # image = db.Column(db.String(200), nullable=True) # Profile Picture > Passport [cloudinary]

    # TIMESTAMP
    timeStamp = db.Column(
        db.DateTime, default=datetime.datetime.utcnow)  # Auto-Generated

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(SECRET_KEY, expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod  # Because we didn't use self in the parameters
    def verify_reset_token(token):
        s = Serializer(SECRET_KEY)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None

        return User.query.get(user_id)

class Consumption(db.Model):
    __tablename__ = 'consumption'  # Explicit is better than implicit.

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True) # user.id = 1 || DB Relationship
    actual_cost_today = db.Column(db.Integer, nullable=False)  # KES. 850
    projected_monthly_cost = db.Column(db.Integer, nullable=False)  # KES. 1350
    previous_cost_saving = db.Column(db.Integer, nullable=False)  # KES. 520
    date = db.Column(db.String(100), nullable=True) # keep track of 'today'
    
    # TIMESTAMP
    timeStamp = db.Column(
        db.DateTime, default=datetime.datetime.utcnow)  # Auto-Generated


class WaterForecast(db.Model):
    __tablename__ = 'water_forecast'  # Explicit is better than implicit.

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True) # user.id = 1 || DB Relationship
    
    projected_weekly_water = db.Column(JSON, nullable=False)  # KES. 1350
    
    date = db.Column(db.String(100), nullable=True) # keep track of 'next week'
    
    # TIMESTAMP
    timeStamp = db.Column(
        db.DateTime, default=datetime.datetime.utcnow)  # Auto-Generated
