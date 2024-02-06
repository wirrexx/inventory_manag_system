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



