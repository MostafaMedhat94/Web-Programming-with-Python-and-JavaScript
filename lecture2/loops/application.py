from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Mostafa', 'Manar', 'Saadon']

    return render_template('index.html', names=names)
