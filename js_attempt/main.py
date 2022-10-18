from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'icytorsecret'

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/surprise')
def surprise():
    return render_template('surprise.html')

if __name__ == '__main__':
    app.run()