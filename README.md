# Smart Waste Management System (SWMS)

## Overview
The Smart Waste Management System is an innovative web application designed to enhance waste collection, recycling, and resource management through intelligent technologies. Users can manage waste collection schedules, track recycling efforts, and view environmental impact metrics. The system supports three primary user roles: Household Users, Waste Collection Services, and Administrators.

## Authors
This project has five authors:
1. Jeremiah Olaitan Agbaje (j.agbaje@alustudent.com)
2. Joan Keza (j.keza1@alustudent.com)
3. Simeon Azeh KONGNYUY (s.kongnyuy@alustudent.com)
4. Palvis Paul Ntawukamenya (p.ntawukame@alustudent.com)
5. Afsa Umutoniwase (a.umutoniwa@alustudent.com)

## Features
- **User Registration and Login**: Secure authentication for users.
- **Waste Collection Scheduling**: Users can schedule waste collections and receive notifications.
- **Recycling Tracking**: Users can track their recycling efforts and view their environmental impact.
- **Waste Collection Services Management**: Manage routes, schedules, and track performance.
- **Admin Dashboard**: Monitor overall system performance and manage users.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **CI/CD**: GitHub Actions
- **Deployment**: Heroku

## Project Structure

SMWS_Group10/

├── app/

│   ├── __init__.py

│   ├── models.py

│   ├── routes/

│   │   ├── __init__.py

│   │   ├── auth.py

│   │   ├── schedule.py

│   │   ├── recycling.py

│   │   ├── services.py

│   │   ├── admin.py

│   ├── templates/

│   │   ├── authentication/

│   │   │   ├── getstarted.html

│   │   ├── dashboard.html

│   │   ├── nav/

│   │   │   ├── services/

│   │   │   │   ├── smartwm.html

│   │   │   │   ├── wastepickup.html

│   │   │   ├── about.html

│   │   │   ├── contact.html

│   │   ├── index.html

│   ├── static/

│   │   ├── assets/

│   │   │   ├── (a bunch of jpg)

│   │   ├── css/

│   │   │   ├── dashboard.css

│   │   │   ├── media.css

│   │   │   ├── reg.css

│   │   │   ├── style.css

│   │   ├── js/

│   │   │   ├── chartjs.js

│   │   │   ├── dashboard.js

│   │   │   ├── index.js

│   │   │   ├── jquery.js

│   │   │   ├── login.js

├── migrations/

├── tests/

│   ├── __init__.py

│   ├── test_auth.py

│   ├── test_schedule.py

│   ├── test_recycling.py

│   ├── test_services.py

│   ├── test_admin.py

├── .github/

│   ├── workflows/

│   │   ├── ci.yml

├── .gitignore

├── config.py

├── requirements.txt

├── run.py

├── README.md


## Setup and Installation

### Prerequisites
- Python 3.8+
- MySQL
- Node.js and npm 

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Afsaumutoniwase/SMWS_Group10.git
   cd SMWS_Group10

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt


4. **Set environment variables:**
    Create a .env file in the root directory of your project and add the following variables:
    ```bash
    FLASK_APP=run.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    DATABASE_URL=mysql+pymysql://username:password@localhost/db_name

5. **Run the application:**

    ```bash
    flask run

## Deployment
### Heroku

1. **Install the Heroku CLI and login:**
    ```bash
    heroku login
2. **Create a new Heroku app:**
    ```bash
    heroku create your-app-name
3. **Set environment variables:**
    ```bash
    heroku config:set SECRET_KEY=your_secret_key
    heroku config:set DATABASE_URL=mysql+pymysql://username:password@hostname/db_name
4. **Deploy the application:**
    ```bash
    git push heroku main

## CI/CD
**GitHub Actions:** This project uses GitHub Actions for continuous integration and deployment. The configuration is in .github/workflows/ci.yml.

## Testing
### Running Tests
1. **To run the unit tests, use:** first Ensure you have tests in the tests directory covering your application's critical parts.
    ```bash     
    git push heroku main
## Contributing

Feel free to contribute by creating pull requests or opening issues. Make sure to follow the project's code style and write tests for new features or bug fixes.

## License
This project is licensed under the MIT License.
This version of the `README.md` includes all essential information about the project in a clear and organized manner. It should provide new developers and contributors with everything they need to understand, set up, and work on the project.