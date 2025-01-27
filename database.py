# database.py
import sqlite3

def create_table():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  description TEXT,
                  amount REAL,
                  date TEXT,
                  category TEXT)''')
    conn.commit()
    conn.close()

def add_expense(description, amount, date, category):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (description, amount, date, category) VALUES (?, ?, ?, ?)",
              (description, amount, date, category))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    conn.close()
    return expenses

def delete_expense(exp_id):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id=?", (exp_id,))
    conn.commit()
    conn.close()

def update_expense(exp_id, new_amount, new_category):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("UPDATE expenses SET amount=?, category=? WHERE id=?",
              (new_amount, new_category, exp_id))
    conn.commit()
    conn.close()
