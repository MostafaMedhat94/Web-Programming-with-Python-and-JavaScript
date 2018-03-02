class Flight:

    counter = 0

    def __init__(self, origin, destination, duration):

        # Keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers.
        self.passengers = []

        # Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f'Flight origin:{self.origin}')
        print(f'Flight destination:{self.destination}')
        print(f'Flight duration:{self.duration}')

        print()
        print('Passengers:')
        for passenger in self.passengers:
            print(f'{passenger.name}')
        print()
    
    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        passenger.flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name

def main():

    #Create a flight.
    f1 = Flight('New York', 'London', 540)
    f2 = Flight('Cairo', 'Rome', 480)
    f3 = Flight('Paris', 'Madrid', 100)

    #Create passengers.
    mostafa = Passenger('Mostafa')
    mohamed = Passenger('Mohamed')
    tareq = Passenger('Tareq')
    radwan = Passenger('Radwan')
    saadon = Passenger('Saadon')
    naser = Passenger('Naser')

    # Add passengers
    f1.add_passenger(mostafa)
    f1.add_passenger(mohamed)
    f2.add_passenger(tareq)
    f2.add_passenger(radwan)
    f3.add_passenger(saadon)
    f3.add_passenger(naser)

    f1.print_info()
    f2.print_info()
    f3.print_info()

    print(f'{mostafa.flight_id}')
    print(f'{mohamed.flight_id}')
    print(f'{tareq.flight_id}')
    print(f'{radwan.flight_id}')
    print(f'{saadon.flight_id}')
    print(f'{naser.flight_id}')
    
if __name__ == '__main__':
    main()