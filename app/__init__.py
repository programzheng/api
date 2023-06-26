from models import db, migrate
from flask import Flask, request
from config import config
from services.auth_service import create_user

app = Flask(__name__)

database_uri = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(config.get("DB_USERNAME"), config.get(
    "DB_PASSWORD"), config.get("DB_HOST"), config.get("DB_PORT"), config.get("DB_DATABASE"))
print(f"DATABASE_URI: {database_uri}")
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)


@app.route('/auth/register', methods=['POST'])
def register():
    create_user(request.json.get('username'), request.json.get('password'))
