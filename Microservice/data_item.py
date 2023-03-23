import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_item.db")

def item_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT *
        FROM item 
        ORDER BY category
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'category': row[0],
            'name': row[1],
            'price': row[2],
            'instock': row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def find_item(category):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT *
        FROM item 
        WHERE category=?
    """
    val = (category,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'category': rows[0],
        'name': rows[1],
        'price': rows[2],
        'instock': rows[3]
        }
    data.append(record)
    
    conn.close()
    return data

def add_item(category,name,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO item(category,name,price,instock)
        VALUES(?,?,?,?)
    """
    val = (category,name,price,instock)
    cursor = conn.execute(sql,val)
    conn.commit()
    conn.close()
    return "Created successfully"

def update_item(category,name,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE item
        SET name=?, price=?, instock=?
        WHERE category=?
    """
    val = (category,name,price,instock)
    cursor = conn.execute(sql,val)
    conn.commit()
    conn.close()
    return "Updated successfully"

def delete_item(category):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM item 
        WHERE category=?
    """
    val = (category,)
    cursor = conn.execute(sql,val)
    conn.commit()
    conn.close()
    return data