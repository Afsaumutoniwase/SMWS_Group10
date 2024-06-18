from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

FLASK_APP = os.getenv('FLASK_APP')
FLASK_ENV = os.getenv('FLASK_ENV')
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()