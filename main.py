from flask import Flask, render_template, request, url_for, redirect
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import auth
import pyrebase
from flask_moment import Moment
from datetime import datetime

config = {
    "apiKey": "AIzaSyDz5RmIwF3xA1TfBePVy6VK0g0Q583LO_c",
    "authDomain": "austin-poetry-writing.firebaseapp.com",
    # "databaseURL": "your_database_url",
    "projectId": "austin-poetry-writing",
    "storageBucket": "austin-poetry-writing.appspot.com",
    "messagingSenderId": "882267327621",
    "appId": "1:882267327621:web:a0b08aab43b84d68d46dec",
    "measurementId" : "G-E7BFJF0087"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)
moment = Moment(app)
cred = credentials.Certificate('path/to/your/firebase-adminsdk.json')
firebase_admin.initialize_app(cred)
db_firestore = firestore.client()

@app.route('/')
def home():
    pass  # Implement this

@app.route('/poems/')
def poems():
    pass  # Implement this

@app.route('/poem/<poem_id>/')
def poem(poem_id):
    pass  # Implement this

@app.route('/search/')
def search():
    pass  # Implement this

if __name__ == '__main__':
    app.run(debug=True)
