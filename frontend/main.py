#main.py
from flask import Flask, jsonify, request
from db import content_homepage, content_songs, content_songs_rock

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return content_homepage()

@app.route('/songs', methods=['GET'])
def songs():
    return content_songs()

@app.route('/songs/rock', methods=['GET'])
def songs_rock():
    return content_songs_rock()

"""
@app.route('/github/intermittents', methods=['GET'])
def github_intermittents():
    return get_github_intermittents()
"""

if __name__ == '__main__':
    app.run()
