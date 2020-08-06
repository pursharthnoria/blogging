import sqlite3

def connect():
    conn = sqlite3.connect("blogging.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,email TEXT, password TEXT,name TEXT, address TEXT,city TEXT,state TEXT,zip TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY,user INTEGER,user_name TEXT,user_email TEXT,date date,multimedia text)")
    conn.commit()
    conn.close()

def insert(email,password,name,address,city,state,zip):
    conn = sqlite3.connect("blogging.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES(NULL,?,?,?,?,?,?,?)",(email,password,name,address,city,state,zip))
    conn.commit()
    conn.close()

def search(email,password):
    conn = sqlite3.connect("blogging.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=? and password=?",(email,password))
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_in_post(user,user_name,user_email,date,multimedia):
    conn = sqlite3.connect("blogging.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES(NULL,?,?,?,?,?,?,?)",(email,password,name,address,city,state,zip))
    conn.commit()
    conn.close()
