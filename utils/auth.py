from app.models.user import User
from flask_jwt_extended import create_access_token

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return create_access_token(identity=user.id)
    return None
