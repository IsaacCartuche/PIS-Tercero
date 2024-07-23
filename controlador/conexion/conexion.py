import cx_Oracle

class Conexion:
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn
        self.connection = None

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(self.username, self.password, self.dsn)
            print("Connected to Oracle Database")
        except cx_Oracle.Error as error:
            print(f"Error connecting to Oracle Database: {error}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from Oracle Database")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            return results
        except cx_Oracle.Error as error:
            print(f"Error executing query: {error}")
            return None

    def execute_dml(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except cx_Oracle.Error as error:
            print(f"Error executing DML: {error}")
            self.connection.rollback()
            return False