import string
import random
import csv
import time
import os
from zipfile import ZipFile

from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="51879a5eff3546faa9292eb3c0dc9cd4",
                                                           client_secret="bd84dca34bc548e1aac7b439ac36c21f"))

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'icytorsecret'

playlist_loaded = 0
playlist = None
playlist_name = ""
playlist_tracks = 0
playlist_downloaded = 0

def load(playlist_id):
    global playlist
    global playlist_loaded
    global playlist_tracks
    global playlist_name

    playlist = sp.playlist_tracks(playlist_id)
    playlist_loaded = 1
    playlist_tracks = len(playlist['items'])

def export(playlist_id):
    playlist_songs = playlist['items']

    tracks = [["index", "name", "album", "artist"]]

    for i in range(len(playlist_songs)):
        tracks.append([i, playlist_songs[i]['track']['name'],
                          playlist_songs[i]['track']['album']['name'],
                          playlist_songs[i]['track']['artists'][0]['name']])

    with open ('data/playlist.csv','w',newline = '') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ',')
        my_writer.writerows(tracks)

def download(playlist_id):
    playlist_songs = playlist['items']

    global playlist_downloaded
    #playlist_songs[0]['track']['external_urls']['spotify'] URL OF TRACK
    
    for i in range(len(playlist_songs)):
        os.system("cd data/playlist && spotdl " + playlist_songs[i]['track']['external_urls']['spotify'])
        playlist_downloaded += 1

    dirs = os.listdir("data/playlist")

    zf = ZipFile('playlist.zip', "w")
    for file in dirs:
        zf.write("data/playlist/" + file)

# Routes
@app.route('/')
def index():
    #6RjXi4FCPU0T6GoSmX58Wu
    #4VtNogIZ8h7PSIR1RMhnCa
    return render_template('index.html')

@app.route('/get_vars', methods = ['GET', 'POST'])
def get_vars():
    return jsonify({'playlist_loaded': playlist_loaded, 'playlist_name': playlist_name, 'playlist_tracks': playlist_tracks, 'playlist_downloaded': playlist_downloaded})

@app.route('/load_playlist/<playlist_id>', methods = ['GET', 'POST'])
def load_playlist(playlist_id):
    load(playlist_id)
    return jsonify({'playlist_loaded': playlist_loaded, 'playlist_tracks': playlist_tracks})

@app.route('/export_playlist/<playlist_id>', methods = ['GET', 'POST'])
def export_playlist(playlist_id):
    if playlist_loaded == True:
        export(playlist_id)
        return send_file("data/playlist.csv", as_attachment=True)
    else:
        return ""

@app.route('/download_playlist/<playlist_id>', methods = ['GET', 'POST'])
def download_playlist(playlist_id):
    if playlist_loaded == True:
        download(playlist_id)
    
    return send_file("playlist.zip", as_attachment=True)

@app.route('/new_playlist', methods = ['GET', 'POST'])
def new_playlist(playlist_id):
    global playlist
    global playlist_loaded
    global playlist_tracks
    global playlist_name
    global playlist_downloaded

    playlist = None
    playlist_loaded = 0
    playlist_tracks = 0
    playlist_name = ""
    playlist_downloaded = 0

    return ""

if __name__ == '__main__':
    app.run()