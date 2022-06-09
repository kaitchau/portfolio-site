import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


isKayla = True

@app.route('/')
def kaitlyn_index():
    return render_template('kaitlyn_index.html', url=os.getenv("URL"))

@app.route('/kaitlyn_about')
def kaitlyn_about():
    return render_template('kaitlyn_about.html', url=os.getenv("URL"))

@app.route('/kaitlyn_experience')
def kaitlyn_experience():
    return render_template('kaitlyn_experience.html', url=os.getenv("URL"))

@app.route('/kaitlyn_education')
def kaitlyn_education():
    return render_template('kaitlyn_education.html', url=os.getenv("URL"))

@app.route('/kaitlyn_hobbies')
def kaitlyn_hobbies():
    return render_template('kaitlyn_hobbies.html', url=os.getenv("URL"))

@app.route('/kaitlyn_places')
def kaitlyn_places():
    return render_template('kaitlyn_places.html', url=os.getenv("URL"))


