class Flights:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")


def main():

    #create Flight
    flight1 = Flights(origin='New York', destination='Paris', duration=540)

    flight2 = Flights(origin="Yae", destination="Yangon", duration=900)

    flight1.duration = 550

    flight1.print_info()

    flight2.print_info()


if __name__ == "__main__":
    main()