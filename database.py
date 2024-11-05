# database.py

import sqlite3

# Database connection setup
def get_connection():
    conn = sqlite3.connect("chocolate_house.db")
    return conn

# Initialize database tables
def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                        id INTEGER PRIMARY KEY,
                        flavor TEXT NOT NULL,
                        available BOOLEAN NOT NULL)''')
                        
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL)''')
                        
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                        id INTEGER PRIMARY KEY,
                        suggestion TEXT NOT NULL,
                        allergy_warning TEXT)''')
    
    conn.commit()
    conn.close()

# CRUD functions for seasonal flavors
def add_seasonal_flavor(flavor, available):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO seasonal_flavors (flavor, available) VALUES (?, ?)", (flavor, available))
    conn.commit()
    conn.close()

def get_seasonal_flavors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

# CRUD functions for ingredients
def add_ingredient(name, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()

def get_ingredients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredients")
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

# CRUD functions for customer suggestions
def add_customer_suggestion(suggestion, allergy_warning):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customer_suggestions (suggestion, allergy_warning) VALUES (?, ?)", (suggestion, allergy_warning))
    conn.commit()
    conn.close()

def get_customer_suggestions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_suggestions")
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions

# Initialize database tables on first run
initialize_database()