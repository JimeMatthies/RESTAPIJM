from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
import os

from routes.main import bpMain
from routes.users import bpUsers

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICACIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost:3306/StarWars"

db.init_app(app)
Migrate(app, db)

app.register_blueprint(bpMain)
app.register_blueprint(bpUsers)

if __name__ == '__main__':
    app.run()