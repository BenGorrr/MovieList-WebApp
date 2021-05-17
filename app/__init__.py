from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7962172ceff48bc8db826ba6d9f21f1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from app import routes
