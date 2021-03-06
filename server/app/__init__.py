"""Initalize Flask package"""
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config.Config')
bootstrap = Bootstrap(app)

from app import routes