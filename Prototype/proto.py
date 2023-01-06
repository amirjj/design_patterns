

class Hall:
    def __init__(self, capacity):
        self.capacity = capacity


class Movie:
    pass


class Time:
    pass


class Seat:
    def __init__(self, number):
        self.number = number


class Sans:
    def __init__(self, movie, hall, time):
        self.movie = movie
        self.hall = hall
        self.time = time
        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):
        """prototype all seats of the selected Hall"""
        for i in range(self.hall.capacity):
            self.seats.append(Seat(i))


if __name__ == "__main__":
    movie = Movie()
    time = Time()
    hall = Hall(60)
    sans = Sans(movie, hall, time)
    print(len(sans.seats))
    print(sans.seats)
    print(sans.seats[0].number)
    print(type(sans.seats[0]))
