import string
import random
import csv

from flask import Flask, render_template, request, redirect, url_for, session, send_file

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="51879a5eff3546faa9292eb3c0dc9cd4",
                                                           client_secret="bd84dca34bc548e1aac7b439ac36c21f"))

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'icytorsecret'

def export(playlist_id):
    playlist_tracks = sp.playlist_tracks(playlist_id)
    playlist_tracks = playlist_tracks['items']

    tracks = [["index", "name", "album", "artist"]]

    for i in range(len(playlist_tracks)):
        tracks.append([i, playlist_tracks[i]['track']['name'],
                          playlist_tracks[i]['track']['album']['name'],
                          playlist_tracks[i]['track']['artists'][0]['name']])

    with open ('playlist.csv','w',newline = '') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ',')
        my_writer.writerows(tracks)

# Routes
@app.route('/')
def index():
    #6RjXi4FCPU0T6GoSmX58Wu
    return render_template('index.html')

@app.route('/export_playlist/<playlist_id>', methods = ['GET', 'POST'])
def export_playlist(playlist_id):
    export(playlist_id)
    return send_file("playlist.csv", as_attachment=True)

if __name__ == '__main__':
    app.run()