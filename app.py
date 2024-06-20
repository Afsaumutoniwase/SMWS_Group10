from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

# Load environment variables
# SECRET_KEY = os.getenv('SECRET_KEY')
# DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///smws.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    result = db.session.execute(db.select(User).where(User.id == int(user_id)))
    user = result.scalar()
    return user


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(1000))
    phone_number: Mapped[int] = mapped_column(Integer)


with app.app_context():
    db.create_all()


# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# db = SQLAlchemy(app)
# app.template_folder = 'app/templates'
# app.static_folder = 'app/static'

# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(20), unique=True, nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=False)
# #     password = db.Column(db.String(60), nullable=False)
# #     posts = db.relationship('Post', backref='author', lazy=True)
# #     schedule = db.relationship('Schedule', backref='responsible_user', lazy=True)
# #     recycling_Transactions = db.relationship('Recycling_Transactions', backref='user_id', lazy=True)

# #     def __repr__(self):
# #         return f"User('{self.username}', '{self.email}')"

# class Roles(db.Model):
#     role_id = db.Column(db.Integer, primary_key=True)
#     role_name = db.Column(db.String(20), unique=True, nullable=False)
#     description = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f"Roles('{self.role_name}', '{self.description}')"

# class Waste_Bins(db.Model):
#     bin_id = db.Column(db.Integer, primary_key=True)
#     location = db.Column(db.String(120), unique=True, nullable=False)
#     capacity = db.Column(db.Integer, primary_key=True)
#     current_level = db.Column(db.Integer, primary_key=True)
#     last_collected = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     bin_type_id = db.Column(db.Integer, db.ForeignKey('bin_types.bin_type_id'), nullable=False)
#     Schedule = db.relationship('Waste_Bins', backref='bin_id', lazy=True)
#     Collected_Waste = db.relationship('Waste_Bins', backref='bin_id', lazy=True)


#     def __repr__(self):
#         return f"Waste_Bins('{self.bin_id}', '{self.location}', '{self.current_level}')"

# class Bin_Types(db.Model):
#     bin_type_id = db.Column(db.Integer, primary_key=True)
#     type_name = db.Column(db.String(20), unique=True, nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     Waste_Bins = db.relationship('Waste_Bins', backref='bin_type', lazy=True)

#     def __repr__(self):
#         return f"Bin_Types('{self.type_name}', '{self.description}')"

#     class Schedule(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         bin_id = db.Column(db.Integer, db.ForeignKey('Waste_Bins.bin_id'), nullable=False)
#         collection_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#         collection_frequency = db.Column(db.String(120), unique=True, nullable=False)
#         collection_status = db.Column(db.String(120), unique=True, nullable=False)
#         responsible_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#         def __repr__(self):
#             return f"Schedule('{self.bin_id}', '{self.collection_date}')"

# class Collected_Waste(db.Model):
#         collection_id = db.Column(db.Integer, primary_key=True)
#         bin_id = db.Column(db.Integer, db.ForeignKey('Waste_Bins.bin_id'), nullable=False)
#         collection_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#         collection_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#         weight = db.Column(db.Integer, primary_key=True)
#         notes = db.Column(db.Text, nullable=False)

#         def __repr__(self):
#             return f"Collected_Waste('{self.collection_id}', '{self.collection_by_user_id}')"

# class Recycling_Centers(db.Model):
#         center_id = db.Column(db.Integer, primary_key=True)
#         location = db.Column(db.String(120), unique=True, nullable=False)
#         contact_info = db.Column(db.String(120), unique=True, nullable=False)
#         operating_hours = db.Column(db.String(120), unique=True, nullable=False)

#         def __repr__(self):
#             return f"Recycling_Centers('{self.center_id}', '{self.location}')"

# class Recycled_Materials(db.Model):
#         material_id = db.Column(db.Integer, primary_key=True)
#         material_name = db.Column(db.String(120), unique=True, nullable=False)
#         description = db.Column(db.Text, nullable=False)
#         recycling_Transactions = db.relationship('Recycling_Transactions', backref='material_id', lazy=True)

#         def __repr__(self):
#             return f"Recycled_Materials('{self.material_id}', '{self.material_name}')"

# class Recycling_Transactions(db.Model):
#         transaction_id = db.Column(db.Integer, primary_key=True)
#         user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#         material_id = db.Column(db.Integer, db.ForeignKey('Recycled_Materials.id'), nullable=False)
#         quantity = db.Column(db.String(120), unique=True, nullable=False)
#         transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#         note = db.Column(db.Text, nullable=False)

#         def __repr__(self):
#             return f"Recycling_Transactions('{self.transaction_id_id}', '{self.user_id}', '{self.transaction_date}')"

# class Posts(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    # if request.method == 'POST':
    #     user_email = request.form.get('email')
    #     user_password = request.form.get('password')
    #
    #     result = db.session.execute(db.select(User).where(User.email == user_email))
    #     user = result.scalar()
    #
    #     if not user:
    #         flash("That email does not exist, please try again.")
    #         return redirect(url_for('login'))
    #     elif not check_password_hash(user.password, user_password):
    #         flash('Password incorrect, please try again.')
    #         return redirect(url_for('login'))
    #     else:
    #         login_user(user)
    #         return redirect(url_for('home'))

    return render_template('authentication/getstarted.html')


@app.route('/sign-up')
def signup():
    return render_template('authentication/getstarted.html')


@app.route('/register')
def register():
    # if request.method == 'POST':
    #     user_name = request.form.get('name')
    #     user_email = request.form.get('email')
    #     user_password = request.form.get('password')
    #     confirm_password = request.form.get('confirm_password')
    #
    #     if user_password != confirm_password:
    #         flash("Passwords do not match, please try again.")
    #         return redirect(url_for('register'))
    #
    #     existing_user = User.query.filter_by(email=user_email).first()
    #     if existing_user:
    #         flash("Email already registered, please log in.")
    #         return redirect(url_for('login'))
    #
    #     hashed_password = generate_password_hash(user_password, method='sha256')
    #     new_user = User(name=user_name, email=user_email, password=hashed_password)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     flash('Registration successful! Please log in.')
    #     return redirect(url_for('login'))
    return render_template('authentication/getstarted.html')


@app.route('/services')
def services():
    return render_template('nav/services.html')


@app.route('/waste_pickip')
def wastepickup():
    return render_template('nav/services/wastepickup.html')


@app.route('/smart_waste_management')
def smartwm():
    return render_template('nav/services/smartwm.html')


@app.route('/about_us')
def about():
    return render_template('nav/about.html')


@app.route('/contact_us')
def contact():
    return render_template('nav/contact.html')


@app.route('/waste_collection_schedule')
def wcs():
    return render_template('wcs.html')


@app.route('/recycling_tracker/<num>')
def rec_tracker(num):
    return render_template('rectracker.html')


@app.route("/notifications")
def notify():
    return render_template('notifications.html')


@app.route("/dashboard/<num>")
def dashboard(num):
    return render_template('dashboard.html')


if __name__ == "__main__":
    # if not os.path.exists('instance'):
    #     os.makedirs('instance')
    #
    # with app.app_context():
    #     db.create_all()
    #     print("Database tables created successfully.")

    app.run(debug=True, host='127.0.0.1', port=8000)
