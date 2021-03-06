import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://grandma:LaHiguera@localhost/grandma')
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute('SELECT id, origin, destination, duration FROM flights').fetchall()
    for flight in flights:
        print(f'Flight {flight.id}: {flight.origin} to {flight.destination} lasting {flight.duration} minutes.')
    
    # prompt the user to choose a flight.
    flight_id = int(input('\nFlight ID: '))
    flight = db.execute('SELECT origin, destination, duration FROM flights WHERE id = :id', 
                        {'id': flight_id}).fetchone()
    
    if flight is None:
        print('Error, no such flight.')
        return
    
    passengers = db.execute('SELECT name FROM passengers WHERE flight_id = :flight_id',
                            {'flight_id': flight_id}).fetchall()
    
    if len(passengers) > 0:
        for passenger in passengers:
            print(passenger.name)
    else:
        print('No passengers.')

if __name__ == '__main__':
    main()