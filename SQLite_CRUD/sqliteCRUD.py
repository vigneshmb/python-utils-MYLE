from db_init import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value REAL,
            quality TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_tag(name, value, quality):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tags (name, value, quality) VALUES (?, ?, ?)",
                (name, value, quality))
    conn.commit()
    conn.close()

def get_all_tags():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tags")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_tag_by_name(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tags WHERE name = ?", (name,))
    row = cur.fetchone()
    conn.close()
    return row

def update_tag_value(name, new_value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tags SET value = ? WHERE name = ?",
                (new_value, name))
    conn.commit()
    conn.close()

def delete_tag(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tags WHERE name = ?", (name,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()

    insert_tag("Pump1.Speed", 1450, "Good")
    insert_tag("Pump1.Status", 1, "Good")

    print("All Records:")
    print(get_all_tags())

    print("Single Record:")
    print(get_tag_by_name("Pump1.Speed"))

    update_tag_value("Pump1.Speed", 1500)
    print("After Update:")
    print(get_tag_by_name("Pump1.Speed"))

    delete_tag("Pump1.Status")
    print("After Delete:")
    print(get_all_tags())
