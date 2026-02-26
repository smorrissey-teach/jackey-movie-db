import sqlite3
conn = sqlite3.connect ("movie.db")
cursor = conn.cursor()

results = cursor.fetchall()

