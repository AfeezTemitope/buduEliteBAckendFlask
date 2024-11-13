from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS
from urls import befa
from models import db  # Assuming db is the SQLAlchemy object
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Register blueprint
app.register_blueprint(befa)

# Initialize the database
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # Create all tables for development (optional for migrations)
    with app.app_context():
        db.create_all()  # Avoid this in production, use migrations instead

    app.run(debug=True)
