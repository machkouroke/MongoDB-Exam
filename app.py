import json

from flask import Flask, render_template, request, redirect, url_for
from config.settings import *
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    f"mongodb+srv://machkouroke:{PASSWORD}@{MONGO_URL}/?retryWrites=true&w=majority")
db = client["Examen"]


@app.route('/')
def index():
    return redirect(url_for('index_with_page', page_number=0))


@app.route('/<int:page_number>')
def index_with_page(page_number: int):
    data = db.games.find().limit(10).skip(page_number * 10)
    return render_template('index.html', games=list(data))


@app.route('/filter', methods=['POST'])
def filter():
    query = json.loads(request.form['filter'])
    data = db.games.find(query)
    return render_template('index.html', games=list(data))


@app.route('/add', methods=['POST'])
def add():
    query = json.loads(request.form['document'])
    db.games.insert_one(query)
    return redirect(url_for('index_with_page', page_number=0))


@app.route('/delete', methods=['POST'])
def delete():
    query = json.loads(request.form['delete-filter'])
    db.games.delete_one(query)
    return redirect(url_for('index_with_page', page_number=0))


@app.route('/update', methods=['POST'])
def update():
    query = json.loads(request.form['filter-update'])
    settings = json.loads(request.form['update-settings'])
    db.games.update_one(query, settings)
    return redirect(url_for('index_with_page', page_number=0))


if __name__ == '__main__':
    app.run(debug=True)
