from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
from flask_moment import Moment
from datetime import datetime
import requests

config = {
    "apiKey": "AIzaSyDz5RmIwF3xA1TfBePVy6VK0g0Q583LO_c",
    "authDomain": "austin-poetry-writing.firebaseapp.com",
    "databaseURL": "https://austin-poetry-writing.firebaseio.com",
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
cred = credentials.Certificate('austin-poetry-writing-firebase-adminsdk-jwfn2-3aa57d33ee.json')
firebase_admin.initialize_app(cred)
db_firestore = firestore.client()

# MEETUP_API_KEY = "your_meetup_api_key"
# GROUP_URL_NAME = "your_group_url_name"

@app.route('/')
def home():
    upcoming_events = get_upcoming_events()
    return render_template("index.html", upcoming_events=upcoming_events)

@app.route('/poems/')
def poems():
    poems = get_all_poems()
    return render_template("poems.html", poems=poems)

@app.route('/poem/<poem_id>/')
def poem(poem_id):
    poem = get_poem(poem_id)
    return render_template("poem.html", poem=poem)

@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        search_results = search_poems(query)
        return render_template("search.html", query=query, search_results=search_results)
    return render_template("search.html")

def get_upcoming_events():
    # url = f"https://api.meetup.com/{GROUP_URL_NAME}/events?&sign=true&photo-host=public&page=20&key={MEETUP_API_KEY}"
    # response = requests.get(url)
    response = [{
        "name": "Childhood Nostalgia",
        "local_date": "Sunday April 16th 2023",
        "local_time": "7pm"
    }]
    return response

def newline_to_paragraph(value):
    lines = value.split('\n')
    return ''.join(f'<p>{line}</p>' for line in lines)

def get_all_poems():
    poems_ref = db_firestore.collection('poems')
    docs = poems_ref.stream()
    poems = [doc.to_dict() for doc in docs]
    return poems

def get_poem(poem_id):
    poem_ref = db_firestore.collection('poems').document(poem_id)
    doc = poem_ref.get()
    if doc.exists:
        return doc.to_dict()
    return None

def search_poems(query):
    poems_ref = db_firestore.collection('poems')
    docs = poems_ref.where("keywords", "array_contains", query.lower()).stream()
    results = [doc.to_dict() for doc in docs]
    return results


app.jinja_env.filters['newline_to_paragraph'] = newline_to_paragraph
if __name__ == '__main__':
    app.run(debug=True)
