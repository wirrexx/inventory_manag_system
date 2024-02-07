# here goes the functions for the sql, Please Use virtual env (venv) when working on this code
import sqlite3

# W: create connection, function to establish connection to SQlite database
def create_connection(db_file):
    #variable name
    conn = None
    
    try: 
        conn = sqlite3.connect(db_file)
        print(f'Connected to database: {db_file}')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# W: create table, function to create products table if it does not exists. 

def create_table(conn):
    try: 
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS products
                  (id INGETER PRIMARY KEY, 
                  name TEXT NOT NULL, price REAL NOT NULL)''')
        print('Table "products" created succesfully.')
    except sqlite3.Error as e:
        print(e)

# W: add_products, function to add price name and quantity to a tablet.
# need cursor, need execute to insert stuff and commit, how to do this??? . 

def add_product(conn, product_id, product_name, quantity, price):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO products (product_id, product_name, quantity, price)
                          VALUES (?, ?, ?, ?)''', (product_id, product_name, quantity, price))
        conn.commit()
        print("Product added successfully!")
    except sqlite3.Error as e:
        print("Error:", e)

db_file = 'inventory.db'

conn = create_connection(db_file)

if conn is not None:
    create_table(conn)
    
    # Example
    product_name = "Sponge Bob"
    product_id = 10001
    quantity = 10
    price = 19.99

    add_product(conn, product_id, product_name, quantity, price)

    conn.close()
else:
    print("Unable to establish database connection.")

