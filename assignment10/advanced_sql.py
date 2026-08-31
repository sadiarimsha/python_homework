import sqlite3

try:
    with  sqlite3.connect('../db/lesson.db') as conn:
        print("Database created and connected successfully.")
        cursor = conn.cursor()

        # Task 1: Complex JOINs with Aggregation
        query = """
        SELECT o.order_id, 
            SUM (p.price * li.quantity) AS total_price
            FROM orders AS o
        JOIN line_items AS li
            ON o.order_id = li.order_id
        JOIN products AS p 
            ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id ASC
        LIMIT 5;
        """
        cursor.execute(query)
        print(cursor.fetchall())

        # Task 2: Understanding Subqueries
        query = """
        SELECT c.customer_name, 
            AVG(ap.total_price) AS average_total_price
        FROM customers AS c
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b,
                SUM(p.price * li.quantity) AS total_price
            FROM orders AS o
            JOIN line_items AS li ON o.order_id = li.order_id
            JOIN products AS p ON li.product_id = p.product_id
            GROUP BY o.order_id, o.customer_id
        ) AS ap ON c.customer_id = ap.customer_id_b
        GROUP BY c.customer_id;

        """
        cursor.execute(query)
        print(cursor.fetchall())

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Task 3: An Insert Transaction Based on Data

try:
    with  sqlite3.connect('../db/lesson.db') as conn:
        print("Database created and connected successfully.")
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = 1")

        query = """
        SELECT c.customer_id FROM customers AS c WHERE  c.customer_name = 'Perez and Sons';
        """
        cursor.execute(query)
        customer_id_value = cursor.fetchall()

        query = """
        SELECT e.employee_id FROM employees AS e WHERE  e.first_name = 'Miranda' AND e.last_name = 'Harris';
        """
        cursor.execute(query)
        employee_id_value = cursor.fetchall()

        query = """
        SELECT p.product_id FROM products AS p ORDER BY p.price ASC LIMIT 5;
        """
        cursor.execute(query)
        product_id_value = cursor.fetchall()

        try:
            # Begin transaction: order insert + all 5 line_item inserts as one unit of work
            cursor.execute(" INSERT INTO orders (customer_id, employee_id, date) VALUES ( ? , ? , DATE('now')) RETURNING order_id ",(customer_id_value[0][0], employee_id_value[0][0]) )
            order_id_value = cursor.fetchone()[0]
            cursor.execute(" INSERT INTO line_items (order_id, product_id, quantity) VALUES ( ? , ? , ? )", (order_id_value, product_id_value[0][0], 10))
            cursor.execute(" INSERT INTO line_items (order_id, product_id, quantity) VALUES ( ? , ? , ? )", (order_id_value, product_id_value[1][0], 10))
            cursor.execute(" INSERT INTO line_items (order_id, product_id, quantity) VALUES ( ? , ? , ? )", (order_id_value, product_id_value[2][0], 10))
            cursor.execute(" INSERT INTO line_items (order_id, product_id, quantity) VALUES ( ? , ? , ? )", (order_id_value, product_id_value[3][0], 10))
            cursor.execute(" INSERT INTO line_items (order_id, product_id, quantity) VALUES ( ? , ? , ? )", (order_id_value, product_id_value[4][0], 10))
            conn.commit()

            # End transaction: order and all line_items committed together
        except sqlite3.Error as e:
            conn.rollback() # # rolls back the order insert and any line_items already inserted above
            print("Transaction failed, rolled back:", e)

        query = """
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items AS li
        JOIN products AS p
            ON li.product_id = p.product_id
        WHERE li.order_id = ? ;
        """
        cursor.execute(query,(order_id_value,))
        print(cursor.fetchall())

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Task 4

try:
    with  sqlite3.connect('../db/lesson.db') as conn:
        print("Database created and connected successfully.")
        cursor = conn.cursor()

        query = """
        SELECT e.first_name, e.last_name, e.employee_id, COUNT(o.order_id) AS order_count
        FROM employees AS e
        JOIN orders AS o
            ON o.employee_id = e.employee_id
        GROUP BY e.employee_id
        HAVING order_count > 5;
        """
        cursor.execute(query)
        print(cursor.fetchall())

except sqlite3.Error as e:
    print(f"An error occurred: {e}")