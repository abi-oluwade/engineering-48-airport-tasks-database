from db_connect_airport import *

# Created methods for the passenger table

class AirportPassenger(MSDBConnection):

    # def __init__(self, name, passport_number):
    #     self.name = name
    #     self.passport_number = passport_number
    #     self.passenger_list = []

    def sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

#(TASK: as a USER I can create a passenger (INSERT))
    # 1. Created the method within the airport passenger class to create a new passenger
    # 2. Ask the user to input a first name, last name and passport number, and assinged all these inputs to the
    # appropriately named variable.
    # 3. created the query variable with the INSERT INTO statement that we want the SQL database to execute.
    # 4. supplied that query variable that was assigned to the 'INSERT INTO' statement as an arguement to the sql_query
    # method that was created in the MSDBConnection class.
    # 5. executed the self.sql_commit method to commit the change to the database.
    def create_a_passenger(self):
        new_passenger_first_name = input('Please input passenger name.')
        new_passenger_last_name = input('Please input the passengers passport number.')
        new_passenger_passport_number = input('Please input the passengers passport number')
        query = "INSERT INTO passengers_class (first_name, last_name, passport_number) VALUES ('{}', '{}','{}' )".format(new_passenger_first_name,new_passenger_last_name, new_passenger_passport_number)
        self.sql_query(query)
        self.sql_commit()

    def add_passenger_to_flight(self):
        pass




# new_passenger = AirportPassenger()
# new_passenger = new_passenger.create_a_passenger()
