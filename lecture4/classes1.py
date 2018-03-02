class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():

    # create a flight.
    f = Flight('New York', 'Paris', 540)

    f.duration += 10

    print(f.origin)
    print(f.destination)
    print(f.duration)

if __name__ == '__main__':
    main()