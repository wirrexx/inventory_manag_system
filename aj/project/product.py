from aj.project.sql_file import main

#creating the product, update, list, delete

def add_product(conn, product_name, quantity, price):
    sql = """
        INSERT INTO Products(product_name, quantity, price)
        VALUES(?,?,?);
    """
    cursor = conn.cursor()
    cursor.execute(sql, (product_name, quantity, price))
    conn.commit()
    return cursor.lastrowid

def update_product(conn, product_id, quantity):
    sql = """
        UPDATE Products SET quantity = ?
        WHERE Product_id = ?
    """
    cursor = conn.cursor()
    cursor.execute(sql, (quantity, product_id))
    conn.commit()
    
def list_products(conn):
    sql = " SELECT * FROM Products;"
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
def delete_product(conn, product_id):
    sql = " DELETE FROM Products WHERE Product_id=?"
    cursor = conn.cursor()
    cursor.execute(sql, (product_id))
    conn.commit()
    

