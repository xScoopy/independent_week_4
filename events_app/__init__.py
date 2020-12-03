"""Import packages and modules for initializing our app."""
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from events_app.config import Config

# Some of this undoubtedly looks a little foreign right now.
# That's okay! We'll learn about Flask blueprints & packages
# later.

app = Flask(__name__)
#config statement added
app.config.from_object(Config)


#initialize db
db = SQLAlchemy(app)

from events_app.main.routes import main

app.register_blueprint(main)

# TODO: add your statement to create database tables
with app.app_context():
  db.create_all()