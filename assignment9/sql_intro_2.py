import pandas as pd
import sqlite3

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        sql_statement = """SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price FROM line_items li JOIN products p ON li.product_id = p.product_id"""
        df = pd.read_sql_query(sql_statement, conn)
        print(df.head(5))
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

df['total'] = df['quantity'] * df['price']
print(df.head(5))

result = df.groupby('product_id').agg({'line_item_id': 'count', 'total' : 'sum', 'product_name' : 'first'})
print(result.head(5))

result= result.sort_values(by='product_name')
print(result.head(5))

result.to_csv('order_summary.csv', sep=',', index=True, header=True, encoding=None)