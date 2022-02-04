#Database

import sqlite3

def createdb():
    
    con=sqlite3.connect("RB.db")

    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS bills(ordno text,Fries text,burger text,drinks text,pizza text,SubTotal text,Tax text,Service text,Total text)")

    con.commit()

    print("Database Created Successfully")

    cur.close()

def insert(ordno,Fries,burger,drinks,pizza,SubTotal,Tax,Service,Total):
    
    con=sqlite3.connect("RB.db")

    cur=con.cursor()

    cur.execute("INSERT INTO bills VALUES(?,?,?,?,?,?,?,?,?)",(ordno,Fries,burger,drinks,pizza,SubTotal,Tax,Service,Total))

    print("Record has been successfully added")

    con.commit()

    con.close()

def display():

    con=sqlite3.connect("RB.db")

    cur=con.cursor()

    cur.execute("SELECT * FROM bills")

    rows=cur.fetchall()

    con.close()

    return rows
    
createdb()
