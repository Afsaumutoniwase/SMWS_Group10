from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

# Load environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///smws.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
app.template_folder = 'app/templates'
app.static_folder = 'app/static'


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




@app.route('/templates/wcs.html')
def wcs():
    return render_template('wcs.html')


@app.route('/templates/rectracker.html')
def rectracker():
    return render_template('rectracker.html')
#
@app.route('/templates/notifications.html')
def notifications():
    return render_template('notifications.html')
#
#
@app.route('/templates/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/templates/settings.html')
def settings():
    return render_template('settings.html')



if __name__ == "__main__":
    # if not os.path.exists('instance'):
    #     os.makedirs('instance')
    # with app.app_context():
    #     db.create_all()
    #     print("Database tables created successfully.")
    app.run(debug=True)
