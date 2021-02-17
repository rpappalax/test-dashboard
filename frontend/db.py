#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        #if os.environ.get('GAE_ENV') == 'standard':
        conn = pymysql.connect(user=db_user, password=db_password,
                            unix_socket=unix_socket, db=db_name,
                            cursorclass=pymysql.cursors.DictCursor
                            )
        return conn
    except pymysql.MySQLError as e:
        print(e)


def content_homepage():
    html = '<html><body><h1>hello</h1></body</html>'
    return html


def content_songs():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute("SELECT * FROM songs")
        songs = cursor.fetchall()
        if result > 0:
            got_songs = jsonify(songs)
        else:
            got_songs = 'No Songs in DB'
    conn.close()
    return got_songs


def content_songs_rock():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute("SELECT * FROM songs WHERE genre = 'Rock'")
        songs = cursor.fetchall()
        if result > 0:
            got_songs = jsonify(songs)
        else:
            got_songs = 'No Songs in DB'
    conn.close()
    return got_songs

