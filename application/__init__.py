from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#INITIALIZING
db = SQLAlchemy()
DB_NAME = "database.db"

#CREATE APP FUNCTION WHCIH RETURNS THE APP WHICH IS CALLED APP.PY FILE TO RUN
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    create_database(app)
    return app


#FUNCTION THAT CHECK IF THE DATABASE IS CREATED OR NOT, IF NOT IT CREATES THE DATABASE
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)