import sqlite3

def create_table():
    conn=sqlite3.connect("test.db")
    cur=conn.cursor() #cursor methon
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("test.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


insert("bowl",10,5)



def view():
    conn=sqlite3.connect("test.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


print(view())


def delete(item):
    conn=sqlite3.connect("test.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


delete("bowl")
print(view())


def update(quantity,price,item):
    conn=sqlite3.connect("test.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?" ,(quantity,price,item))
    conn.commit()
    conn.close()


update(11,6,"Wine Glass")
print(view())
