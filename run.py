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

app.template_folder = 'app/templates'
app.static_folder = 'app/static'


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
    app.run(debug=True)
