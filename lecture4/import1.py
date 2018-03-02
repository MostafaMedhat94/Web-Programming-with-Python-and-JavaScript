import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('tzu')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    f = open('flights.csv')
    reader = csv.reader(f)

    for origin, destination, duration in reader:
        # new Flight instance {object}
        flight = Flight(origin=origin, destination=destination,
                        duration=duration)
        # insert each flight
        db.session.add(flight)
        print(f'Added flight form {origin} to {destination} lasting {duration} minutes.')
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        main()
