import pandas

df = pandas.read_csv("hotels.csv")


class User:
    pass


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        pass

    def book(self):
        pass

    def available(self):
        """ Check if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False




class ReservationTicket:
    def __init__(self, costumer_name, hotel_object):
        pass

    def generate(self):
        contest = f"Name of the costomer hotel"
        return contest


class CreditCard:
    pass


# Main loop
print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
