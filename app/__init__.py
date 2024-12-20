import os
from flask import Flask
from app.models import db
from app.routes import patient_blueprint

def create_app():
    app = Flask(__name__)

    # Retrieve database connection details from environment variables
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASSWORD', 'ec2-54-81-109-229.compute-1.amazonaws.com')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'meditrack')

    # Construct the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Ensure tables are created
    with app.app_context():
        db.create_all()

    app.register_blueprint(patient_blueprint, url_prefix='/patient-record-service/')
    return app
