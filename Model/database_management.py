import sqlite3


class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)

    def insert_data(self, table_name, values):
        query = f"INSERT INTO {table_name} VALUES {values}"
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()


data = (3, 'Matteo')

db = Database('prova')
# db.create_table('Tenants', 'id integer, name text')
db.insert_data('Tenants', data)
print(db.fetch_data('Tenants'))


db.close_connection()
