from flask import Flask, jsonify, request, make_response, session
from flask_migrate import Migrate
from flask_restful import Api, Resource

import random
import datetime

from config import app, db, api
#from models import 

@app.route('/')
def index():
    return '<h1>Shri Guru Ravi Dass Sabha of New York Finances</h1>'