import sqlite3

def connect():
    conn = sqlite3.connect("blogging.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,email TEXT, password TEXT,name TEXT, address TEXT,city TEXT,state TEXT,zip TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY,userid INTEGER,username TEXT,useremail TEXT,dateofupload date,content TEXT,likes INTEGER,dislikes INTEGER)")
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

def insert_in_post(user,user_name,user_email,date,content,likes,dislikes):
    conn = sqlite3.connect("blogging.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO posts VALUES(NULL,?,?,?,?,?,?,?)",(user,user_name,user_email,date,content,likes,dislikes))
    conn.commit()
    conn.close()

def display_all_posts():
    conn = sqlite3.connect('blogging.db')
    cur = conn.cursor()
    cur.execute("Select * from posts order by likes desc")
    rows = cur.fetchall()
    conn.close()
    return rows

def display_user_posts(user_pk):
    conn = sqlite3.connect('blogging.db')
    cur = conn.cursor()
    cur.execute("Select * from posts where userid={}".format(user_pk))
    rows = cur.fetchall()
    conn.close()
    return rows

def updatelikes(post_id):
    conn = sqlite3.connect('blogging.db')
    cur = conn.cursor()
    cur.execute("Update posts set likes=likes+1 where id={}".format(post_id))
    conn.commit()
    conn.close()


def updatedislikes(post_id):
    conn = sqlite3.connect('blogging.db')
    cur = conn.cursor()
    cur.execute("Update posts set dislikes=dislikes+1 where id={}".format(post_id))
    conn.commit()
    conn.close()