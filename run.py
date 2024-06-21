from flask import Flask, render_template, url_for, request, flash, session,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_migrate import Migrate


load_dotenv()

# Load environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'inYiT9ipJ$TAT')
DATABASE_URL = os.getenv('DATABASE_URI', 'sqlite:///instance/smws.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.template_folder = 'app/templates'
app.static_folder = 'app/static'

class User(db.Model):
    name = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/templates/index.html')
def home():
    return render_template('index.html')


@app.route('/templates/authentication/login.html')
def login():
    return render_template('authentication/login.html')


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


@app.route('/templates/wcs.html')
def wcs():
    username = session.get('name', None)
    if not username:
        return redirect('/')
    
    return render_template('wcs.html', username=username)


@app.route('/templates/rectracker.html')
def rectracker():
    username = session.get('name', None)
    if not username:
        return redirect('/')
    
    return render_template('rectracker.html', username=username)

@app.route('/templates/notifications.html')
def notifications():
    username = session.get('name', None)
    if not username:
        return redirect('/')
    
    return render_template('notifications.html', username=username)

@app.route('/templates/settings.html')
def user_settings():
    username = session.get('name', None)
    email = session.get('email', None)
    phone = session.get('phone', None)
    address = session.get('address', None)
    if not username:
        return redirect('/')
    return render_template('settings.html', username=username, email=email, phone=phone, address=address)


@app.route('/templates/authentication/getstarted.html', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        phone = request.form['phone_number']
        
        # Validate form data (you can add more validation)
        if not name or not email or not password or not address or not phone:
            return redirect(url_for('signup'))
        
        # Create a new user
        new_user = User(name=name, email=email, password=password, address=address, phone=phone)
        
        # Add user to the database
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            return redirect(url_for('enter'))
    return render_template('/templates/authentication/getstarted.html')

@app.route('/templates/authentication/login.html', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Query the database for the user
        user = User.query.filter_by(email=email).first()
        
        if user and user.password == password:
            # Password is correct, redirect to dashboard
            session['name'] = user.name
            session['email'] = user.email
            session['address'] = user.address
            session['phone'] = user.phone
            return redirect(url_for('dashboard'))
        else:
            return render_template('/templates/authentication/login.html',error='Invalid credentials')
    return render_template('/templates/authentication/login.html')
@app.route('/templates/dashboard.html')
def dashboard():
    username = session.get('name', None)
    if not username:
        return redirect('/')
    
    # Render dashboard template with username passed as variable
    return render_template('dashboard.html', username=username)

@app.route('/signout')
def signout():
    session.pop('username', None)  # Clear username from session
    return redirect(url_for('signin')) 

if __name__ == "__main__":
    if not os.path.exists('instance'):
        os.makedirs('instance')
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
    app.run(debug=True)