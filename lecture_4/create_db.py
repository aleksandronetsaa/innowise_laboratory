import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

cur.execute("""
SELECT full_name, birth_year 
FROM students 
WHERE birth_year > 2004
""")

print(cur.fetchall())
