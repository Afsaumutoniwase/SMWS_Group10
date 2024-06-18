from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read environment variables
FLASK_APP = os.getenv('FLASK_APP')
FLASK_ENV = os.getenv('FLASK_ENV')
SECRET_KEY = os.getenv('SECRET_KEY')

# Create Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Define route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Other routes can be defined here as per your application structure

if __name__ == "__main__":
    app.run()
