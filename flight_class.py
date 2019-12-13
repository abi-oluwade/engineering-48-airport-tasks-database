from db_connect_airport import *

# created methods for the flights table

class Flight(MSDBConnection):
    # def __init__ (self, # plane_number, origin, destination):
        # super().__init__()
        # self.plane_number = plane_number
        # self.origin = origin
        # self.destination = destination
        # self.passenger_list = []

    def sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

# (TASK:As I user I can list all flights)
    # This method will print all the flights within the flight_class table, it works by doing the following:
    # 1. the method print all flights is defined
    # 2. the query is assigned to the string command we want to give to the database in SQL
    # 3. another variable 'all_flights' is assgined to the method created in the parent class that performs the command on the database.
    # 4. the query is printed one at a time using the while loop until the flight value is None(which is equivalent to 'NULL' in SQL)
    def print_all_flights(self):
        query = 'SELECT * FROM flight_class'
        all_flights = self.sql_query(query)
        while True:
            flight = all_flights.fetchone()
            if flight is None:
                break
            print("Origin: {}, Destination: {}, Flight Number: {} ".format(flight.origin, flight.destination, flight.flight_number))
            # print(f"Origin: {flight.origin}") this is the other way to format it and insert inputs into a string.


flights = Flight()
flights = flights.print_all_flights()
