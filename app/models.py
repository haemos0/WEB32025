from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialisation de la base de données
db = SQLAlchemy()

# Model de l'utilisateur pour la base de données
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model des tokens blacklistés dans la base de données
class BlacklistedToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False, unique=True)
    def __repr__(self):
        return f'<BlacklistedToken {self.token}>'
