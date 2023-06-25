
from models import db, migrate
from flask import Flask
import os
from config import config

app = Flask(__name__)

database_uri = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(config.get("DB_USERNAME"), config.get(
    "DB_PASSWORD"), config.get("DB_HOST"), config.get("DB_PORT"), config.get("DB_DATABASE"))
print(f"DATABASE_URI: {database_uri}")
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def index():
    return config.get("DB_HOST")
