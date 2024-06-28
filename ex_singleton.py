"""
Example of Singleton pattern:
This example demonstrates the Singleton pattern by creating a Database Connection Manager.
The Database Connection Manager ensures that only one instance of the connection exists 
and provides a global point of access to the database connection.
"""

import sqlite3
from sqlite3 import Connection

class DatabaseConnectionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnectionManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.connection = sqlite3.connect(':memory:')
        self._create_tables()

    def _create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def get_connection(self) -> Connection:
        return self.connection

    def add_user(self, username: str, email: str):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
        self.connection.commit()

    def get_users(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, username, email FROM users')
        return cursor.fetchall()

# Function to interact with the database
def interactive_database_manager():
    db_manager = DatabaseConnectionManager()

    while True:
        print("\n--- Database Manager ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            db_manager.add_user(username, email)
            print("User added successfully.")
        elif choice == "2":
            users = db_manager.get_users()
            print("\nCurrent Users:")
            for user in users:
                print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
        elif choice == "3":
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

# Usage
if __name__ == "__main__":
    interactive_database_manager()
