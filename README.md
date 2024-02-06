# inventory_manag_system
AJ, Daniel, Rox, Wisam task 


**Inventory Management System**
*Team Exercise*
# Backstory:
    Your team is tasked with creating a basic inventory management system for a small business.
    The system should allow the user to add, retrieve, update, and delete product information in the SQLite database through a user interface (UI).
    you have the freedom to conduct the task however you and your team see fit.
# Objective:
    -create a SQLite DB that you will populate
    -Build a Python program that interacts with an SQLite database for managing an inventory and includes some kind of user interface (CLI or GUI).
# Bonus:
    - are you able to log who last modified each item in the table?
    - create a single repository on GitHub that will host your application, to ensure your team is working on the same app
# Test Case:
    - is the database accessible?
    - can the user freely Add, Read, Update and Delete items from the database using the UI?
    - does the app work consistently without crashing (are errors caught and handled correctly)


## How can we tackle this? 

    - What are the req: 
    Create and populate SQLite DB 
    
    Split the tasks: 
    how? 

## Wisams task 
    - 3 functions
    - create connection 
    - create table
    - add_product

# So here's my take on it.
What are the req?
    -SQLite3
    -Add
    -Retrieve
    -Update
    -Remove
    -Design the database scheme
    -How do we implement the operations?
    -functions with parameters.

# func for create_connection(db_file):
# This this connect to the sqlite3.connect(db_file)
# func create_table():
# this will execute ('''CREATE TABLE IF NOT EXISTS...)
# func add_product(conn, name, price, quantity):
# this will execute(f'''INSERT INTO products({name}, {price}, {quantity})
# func retrieve_all_prodcuts():
# this will fetchall() in a for loop
# func delete_products(product_id):
# this will execute (f'''DELETE FROM products WHERE ID  = {product_id}''') commit()

## While True
    - then we will have to have a while True:
# ask the user if they want to :
# add
# view
# delete
# exit
# if == 1
# we need to ask user to enter name of product, price and quantity
# call the add_product(name, price, quantity)
# elif == 2:
# retrieve_all_products()
# elif == 3:
# we ask the product id that we want to delete and execute the function:
# delete_products()
# elif == 4:
# we break(exit program)

## we would split the code into different pieces.
### main.py which will have the while true running
### and the sqlite functions
### This way we can easily work on the same code if we do a git repository.

# and split up the task.

## So for my part, I will try to read upon sqlite3 more and how to do things.

