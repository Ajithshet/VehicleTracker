import psycopg2 as pg


class DatabaseManager:
    """
    DatabaseManager class is used to interact with the database for all kinds of queries.
    """

    def __init__(self, dbname, user, password, host, port):
        try:
            self.conn = pg.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.conn.cursor()
        except pg.Error as e:
            print(f"Error connecting to the database - {e}")
            raise ConnectionError(e)

    def __del__(self):  # Destructor used to close the connection - backup method
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def close_all(self):
        """
        Used to close all connection to the database. Primary method for closing connection
        :return:
        """
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def fetch_one_vehicle(self, vehicle_id: int):
        """
        Used to fetch details of one vehicle
        :param vehicle_id: Integer
        :return: Tuple
        """
        try:
            self.cursor.execute("SELECT * FROM vehicles WHERE vehicle_id = %d", (vehicle_id,))
            vehicle = self.cursor.fetchone()
            return vehicle  # Returns a tuple
        except pg.Error as e:
            print(f"Fetching details failed: {e}")
            raise ConnectionError(e)

    def fetch_all(self):
        """
        Used to fetch all vehicles
        :return: List[Tuple]
        """
        try:
            self.cursor.execute("SELECT * FROM vehicles")
            vehicles = self.cursor.fetchall()
            return vehicles
        except pg.Error as e:
            print(f"Fetching details failed: {e}")
            raise ConnectionError(e)

    def fetch_first_vehicle(self):
        """
        Used to fetch the first vehicle to initialize the app
        :return: tuple
        """
        try:
            self.cursor.execute("SELECT * FROM vehicles ORDER BY vehicle_id ASC LIMIT 1")
            vehicle = self.cursor.fetchone()
            return vehicle
        except pg.Error as e:
            print(f"Fetching details failed: {e}")
            raise ConnectionError(e)
