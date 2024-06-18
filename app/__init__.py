from flask import Flask, render_template

app = Flask(__name__)

# Configuration for static files and templates
app.static_folder = 'static'
app.template_folder = 'templates'

# Example route to render a template
@app.route('/')
def index():
    return render_template('index.html')

# Add other routes as per your application structure

if __name__ == '__main__':
    app.run()
