import pyodbc  # alt-shift-enter will install missing modules.


# Created connection

class MSDBConnection():
    def __init__(self):  # Initialized the connection between python and the database.
        self.server = 'localhost,1433'
        self.database = 'Airports'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_Airports = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ''
                                                                                                            ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Airports.cursor()

    def sql_query(self, sql_query):  # __. Makes it private, meaning it can only be called by other methods (due to the
        # double underscore) C.R.U.D = create, read, update, delete
        return self.cursor.execute(sql_query)
    def sql_commit(self):
        return self.cursor.commit()

# row = cursor.fetchone()
# print(row)
# print(cursor.fetchone())
