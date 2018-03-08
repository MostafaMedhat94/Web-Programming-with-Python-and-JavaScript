from flask import Flask, render_template, request
from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('tzu')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    flights = Flight.query.all()
    return render_template('index.html', flights=flights)

@app.route('/book', methods=['POST'])
def book():
    """Book a flight."""

    # Get form information
    name = request.form.get('name')
    try:
        flight_id = int(request.form.get('flight_id'))
    except ValueError:
        return render_template('error.html', error='Invalid flight ID.')
    
    # Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if not flight:
        return render_template('error.html', message='No such flight with that ID.')
    
    # Add passenger
    flight.add_passenger(name)
    return render_template('success.html')

@app.route('/flights')
def flights():
    """List all flights."""

    flights = Flight.query.all()
    return render_template('flights.html', flights=flights)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    """List details about a single flight."""

    # Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template('error.html', message='No such flight with that ID.')
    
    # Get all passengers
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template('flight.html', flight=flight, passengers=passengers)