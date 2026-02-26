import sqlite3
conn = sqlite3.connect ("movie.db")
cursor = conn.cursor()

results = cursor.fetchall()

for row in results:
        genres = row[5]
        movie_id = row[0]
        genres_list = genres.split(',')
        for genre in genres_list:
            cursor.execute('''INSERT OR IGNORE INTO genre (genre_text) VALUES (?)''', (genre,))
            cursor.execute(f'''SELECT id FROM genre WHERE genre_text ="{genre}"''')
            result = cursor.fetchone()
            print(result[0])
            cursor.execute('''INSERT INTO movie_genre (movie_id, genre_id) VALUES (?, ?)''', (movie_id, genre))




conn.commit()