#Task 1

import sqlite3

try:
    with  sqlite3.connect('../db/magazines.db') as conn:
        print("Database created and connected successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()

#Task 2

try:
    with sqlite3.connect('../db/magazines.db') as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                publisher_name TEXT NOT NULL UNIQUE
                )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                magazine_name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                subscriber_name TEXT NOT NULL,
                subscriber_address TEXT NOT NULL
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                expiration_date TEXT NOT NULL,
                subscriber_id INTEGER,
                magazine_id INTEGER,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
            )
        """)
        print("Tables created successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}") 

#Task 3

try:
    with sqlite3.connect('../db/magazines.db') as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        def add_publisher(cursor, publisher_name):
            try:
                cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (publisher_name,))
            except sqlite3.IntegrityError:
                print(f"{publisher_name} is already in the database.")

        def add_magazine(cursor, magazine_name, publisher_name):
            cursor.execute(
                "SELECT publisher_id FROM publishers WHERE publisher_name = ?",
                (publisher_name,)
            )
            result = cursor.fetchone()
            if result is None:
                print(f"There is no publisher named {publisher_name}.")
                return
            publisher_id = result[0]
            try:
                cursor.execute("INSERT INTO magazines (magazine_name, publisher_id) VALUES (?,?)", (magazine_name,publisher_id))
            except sqlite3.IntegrityError:
                print(f"{magazine_name} is already in the database.")

        def add_subscriber(cursor, subscriber_name, subscriber_address):
            cursor.execute(
                "SELECT * FROM subscribers WHERE subscriber_name = ? AND subscriber_address = ?",
                (subscriber_name, subscriber_address)
            )
            if len(cursor.fetchall()) > 0:
                print(f"{subscriber_name} at {subscriber_address} is already in the database.")
                return
            cursor.execute(
                "INSERT INTO subscribers (subscriber_name, subscriber_address) VALUES (?,?)",
                (subscriber_name, subscriber_address,))

        def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name ,expiration_date):
            cursor.execute(
                "SELECT subscriber_id FROM subscribers WHERE subscriber_name = ? AND subscriber_address = ?",
                (subscriber_name, subscriber_address)
            )
            result = cursor.fetchone()
            if result is None:
                print(f"There is no subscriber {subscriber_name} at {subscriber_address}.")
                return
            subscriber_id = result[0]

            cursor.execute(
                "SELECT magazine_id FROM magazines WHERE magazine_name = ?",
                (magazine_name,)
            )
            result = cursor.fetchone()
            if result is None:
                print(f"There is no magazine named {magazine_name}.")
                return
            magazine_id = result[0]

            cursor.execute(
                "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
                (subscriber_id, magazine_id)
            )
            if len(cursor.fetchall()) > 0:
                print(f"{subscriber_name} is already subscribed to {magazine_name}.")
                return

            cursor.execute(
                "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                (subscriber_id, magazine_id, expiration_date)
            )

        add_publisher(cursor, 'NY Magazine')  
        add_publisher(cursor, 'Chicago Magazine')
        add_publisher(cursor, 'DW Papers')

        add_magazine(cursor, 'NY Post', 'NY Magazine')
        add_magazine(cursor, 'Chicago Tribune', 'Chicago Magazine')
        add_magazine(cursor, 'Dawn', 'DW Papers')

        add_subscriber(cursor, 'Jasmine', '123 Apple Ct')
        add_subscriber(cursor, 'Rashid', '45 Sidr Ct')
        add_subscriber(cursor, 'Waheed', '100 Maple Ct')

        add_subscription(cursor, 'Jasmine', '123 Apple Ct', 'NY Post', '12-01-26')
        add_subscription(cursor, 'Rashid', '45 Sidr Ct', 'Chicago Tribune', '10-05-27')
        add_subscription(cursor, 'Waheed', '100 Maple Ct', 'Dawn', '18-02-27')

        conn.commit() 
        print("Sample data inserted successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Task 4
try:
    with sqlite3.connect('../db/magazines.db') as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM subscribers")
        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor.execute("SELECT * FROM magazines ORDER BY magazine_name ASC")
        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor.execute("SELECT m.magazine_name, p.publisher_name FROM magazines AS m JOIN publishers AS p on m.publisher_id = p.publisher_id")
        result = cursor.fetchall()
        for row in result:
            print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Task 5

