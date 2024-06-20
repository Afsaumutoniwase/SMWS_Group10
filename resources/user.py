from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    schedule = db.relationship('Schedule', backref='responsible_user', lazy=True)
    recycling_transactions = db.relationship('Recycling_Transactions', backref='user', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
