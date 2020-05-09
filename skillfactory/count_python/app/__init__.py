from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from config import Config
from flask_migrate import Migrate
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

celery = Celery(app.name,  broker='redis://localhost', backend='redis://localhost')
celery.conf.update(app.config)
migrate = Migrate(app, db)


from app import routes, models,forms
db.create_all()