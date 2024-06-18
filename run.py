from dotenv import load_dotenv
import os

load_dotenv()

# Now you can access the environment variables
FLASK_APP = os.getenv('FLASK_APP')
FLASK_ENV = os.getenv('FLASK_ENV')
SECRET_KEY = os.getenv('SECRET_KEY')
