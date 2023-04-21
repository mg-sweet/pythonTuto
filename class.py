class Flights:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


def main():

    #create Flight
    flight1 = Flights(origin='New York', destination='Paris', duration=540)

    flight1.duration = 550

    print(flight1.origin)
    print(flight1.destination)
    print(flight1.duration)


if __name__ == "__main__":
    main()