from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row  #to fetching a dict results
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM PRODUCTS;').fetchall()
    conn.close()
    return render_template('list_product.html', products=products)

@app.route('/add', methods=('GET', 'POST'))
def add_product():
    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        conn = get_db_connection()
        conn.execute('INSERT INTO products (product_name, quantity, price) VALUES (?, ?, ?)', (product_name, quantity, price))
        conn.commit()
        #conn.close()
        
        # Fetch the updated list of products
        products = conn.execute('SELECT * FROM products;').fetchall()
        #conn.close()

        return render_template('list_product.html', products=products)

    # Handle other HTTP methods if needed
    return redirect(url_for('index'))

@app.route('/update/<int:product_id>', methods=('GET', 'POST'))
def update_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM Products WHERE Product_id = ?', (product_id,)).fetchone()

    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        conn.execute('UPDATE Products SET product_name = ?, quantity = ?, price = ? WHERE product_id = ?', (product_name, quantity, price, product_id))

        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('update_product.html', product=product)

@app.route('/delete/<int:product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM Products WHERE Product_id = ?', (product_id,)).fetchone()

    if request.method == 'POST':
        conn.execute('DELETE FROM Products WHERE product_id = ?', (product_id,))

        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('confirm_delete.html', product_id=product_id, product_name=product['product_name'])

if __name__ == '__main__':
    app.run(debug=True)