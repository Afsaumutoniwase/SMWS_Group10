from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from dotenv import load_dotenv
from datetime import datetime
import os
from flask_admin.contrib.sqla import ModelView

load_dotenv()

# Load environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///instance/smws.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
app.template_folder = 'app/templates'
app.static_folder = 'app/static'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    schedule = db.relationship('Schedule', backref='responsible_user', lazy=True)
    recycling_Transactions = db.relationship('Recycling_Transactions', backref='user_id', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Roles, db.session))
# admin.add_view(ModelView(Waste_Bins, db.session))
# admin.add_view(ModelView(Bin_Types, db.session))
# admin.add_view(ModelView(Collected_Waste, db.session))
# admin.add_view(ModelView(Recycling_Centers, db.session))
# admin.add_view(ModelView(Recycled_Materials, db.session))
# admin.add_view(ModelView(Recycling_Transactions, db.session))
# admin.add_view(ModelView(Posts, db.session))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/index.html')
def home():
    return render_template('index.html')

@app.route('/templates/authentication/getstarted.html')
def login():
    return render_template('authentication/getstarted.html')

@app.route('/templates/authentication/getstarted.html')
def signup():
    return render_template('authentication/getstarted.html')

@app.route('/templates/authentication/getstarted.html')
def register():
    return render_template('authentication/getstarted.html')

@app.route('/templates/nav/services.html')
def services():
    return render_template('nav/services.html')

@app.route('/templates/nav/services/wastepickup.html')
def wastepickup():
    return render_template('nav/services/wastepickup.html')

@app.route('/templates/nav/services/smartwm.html')
def smartwm():
    return render_template('nav/services/smartwm.html')

@app.route('/templates/nav/about.html')
def about():
    return render_template('nav/about.html')

@app.route('/templates/nav/contact.html')
def contact():
    return render_template('nav/contact.html')

if __name__ == "__main__":
    if not os.path.exists('instance'):
        os.makedirs('instance')
    with app.app_context():    
        db.create_all()
        print("Database tables created successfully.")
    app.run(debug=True)
