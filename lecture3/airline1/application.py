import os 

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, flash, render_template, request, redirect,url_for

app = Flask(__name__)
app.secret_key = 'LaHiguera'

engine = create_engine(os.getenv('grandma'))
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    flights = db.execute('SELECT * FROM flights').fetchall()
    return render_template('index.html', flights=flights)

@app.route('/book', methods=['POST'])
def book():
    """Book a Flight."""

    name = request.form.get('name')
    if name == '':
        flash('Please, enter a valid name.')
        return redirect(url_for('index'))

    try:
        flight_id = request.form.get('flight_id')
    except ValueError:
        return render_template('error.html', message='Invalid flight number.')

    # Make sure the flight exists
    if db.execute('SELECT * FROM flights WHERE id = :id', {'id': flight_id}).rowcount == 0:
        return render_template('error.html', message='No such flight with that id!')
    
    # Booking the chosen flight to the passenger
    db.execute('INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)',
               {'name': name, 'flight_id': flight_id})
    db.commit()

    return render_template('success.html')

@app.route('/flights')
def flights():
    """List all flights."""

    flights = db.execute('SELECT * FROM flights').fetchall()
    return render_template('flights.html', flights=flights)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    flight = db.execute('SELECT * FROM flights WHERE id = :id', {'id': flight_id}).fetchone()

    if flight is None:
        return render_template('error.html', message='No such flight.')

    passengers = db.execute('SELECT * FROM passengers WHERE flight_id = :flight_id', {'flight_id': flight_id}).fetchall()
    return render_template('flight.html', flight=flight, passengers=passengers)

