class Flights:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: f{self.origin}")
        print(f"Flight destination: f{self.destination}")
        print(f"Flight duration: f{self.duration}")


def main():

    #create Flight
    flight1 = Flights(origin='New York', destination='Paris', duration=540)

    flight1.duration = 550

    print(flight1.origin)
    print(flight1.destination)
    print(flight1.duration)

    flight1.print_info()


if __name__ == "__main__":
    main()