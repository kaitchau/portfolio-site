import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
load_dotenv()
app = Flask(__name__)


isKaitlyn = True

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

app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
user=os.getenv("MYSQL_USER"),
password=os.getenv("MYSQL_PASSWORD"),
host=os.getenv("MYSQL_HOST"),
port=3306
)

print(mydb)