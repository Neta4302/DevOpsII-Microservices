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
        ORDER BY id
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3],
            'instock': row[4]
            }
        data.append(record)
    
    conn.close()
    return data

def find_item(id):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT *
        FROM item 
        WHERE id=?
    """
    val = (id,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'id': rows[0],
        'name': rows[1],
        'category': rows[2],
        'price': rows[3],
        'instock': rows[4]
        }
    data.append(record)
    
    conn.close()
    return data

def add_item(id,name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO item(id,name,category,price,instock)
        VALUES(?,?,?,?,?)
    """
    val = (id,name,category,price,instock)
    cursor = conn.execute(sql,val)
    conn.commit()
    conn.close()
    return "Created successfully"

def update_item(id,name,category,price,instock):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE item
        SET name=?, category=?, price=?, instock=?
        WHERE id=?
    """
    val = (id,name,category,price,instock)
    cursor = conn.execute(sql,val)
    conn.commit()
    conn.close()
    return "Updated successfully"

def delete_item(id):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM item 
        WHERE id=?
    """
    val = (id,)
    cursor = conn.execute(sql,val)
    conn.commit()
    conn.close()
    return "Deleted successfully"