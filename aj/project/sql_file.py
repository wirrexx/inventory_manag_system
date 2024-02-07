import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as err:
        print(err)
    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as err:
        print(err)

def main():
    database = r"inventory.db"

    sql_create_products_table = """
    CREATE TABLE IF NOT EXISTS Products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
    );
    """

    #create a database connection 
    conn = create_connection(database)

    #create tables
    if conn is not None:
        #create products table
        create_table(conn, sql_create_products_table)
    else:
        print("Error! cannot create the database connection.")

    conn.close()

if __name__ == '__main__':
    main()