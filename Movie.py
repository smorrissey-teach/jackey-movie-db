import csv
import sqlite3
conn = sqlite3.connect ("movie.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
firstname TEXT,
lastname TEXT,
email TEXT,
age TEXT);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS actors(
id INTEGER PRIMARY KEY,
firstname TEXT,
lastname TEXT,
entertainment TEXT);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
id INTEGER PRIMARY KEY,
title TEXT,
mpa_rating INTEGER,
director TEXT,
length INTEGER,
released_date INTEGER,
production_company TEXT,
genre TEXT,
country TEXT);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS genre(
id INTEGER PRIMARY KEY,
genre TEXT);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS reviews(
id INTEGER PRIMARY KEY,
rates INTEGER,
description TEXT,
timestamp INTEGER,
users_id INTEGER,
movies_id INTEGER,
FOREIGN KEY(users_id) references users (id),
FOREIGN KEY(movies_id) REFERENCES movies (id));''')
cursor.execute('''CREATE TABLE IF NOT EXISTS links(
movieId INTEGER PRIMARY KEY,
imbId NUMERIC,
tmbId NUMERIC,
FOREIGN KEY (movieId) references movie (id));''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tags(
id INTEGER PRIMARY KEY,
userId INTEGER,
movieId INTEGER,
tag TEXT,
timestamp INTEGER,
FOREIGN KEY (movieId) references movie (id));''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS actors_movies (
            actors_id INTEGER NOT NULL,
            movies_id INTEGER NOT NULL,
            PRIMARY KEY(actors_id, movies_id),
            FOREIGN KEY(actors_id) REFERENCES actors (id)
                ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(movies_id) REFERENCES movies (id)
                ON DELETE CASCADE ON UPDATE CASCADE
        );
    ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS users_reviews (
            users_id INTEGER NOT NULL,
            reviews_id INTEGER NOT NULL,
            PRIMARY KEY(users_id, reviews_id),
            FOREIGN KEY(users_id) REFERENCES users (id)
                ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(reviews_id) REFERENCES reviews (id)
                ON DELETE CASCADE ON UPDATE CASCADE
        );
    ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies_genre (
            movies_id INTEGER NOT NULL,
            genre_id INTEGER NOT NULL,
            PRIMARY KEY(movies_id, genre_id),
            FOREIGN KEY(movies_id) REFERENCES movies (id)
                ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(genre_id) REFERENCES genre (id)
                ON DELETE CASCADE ON UPDATE CASCADE
        );
    ''')

with open('data/movies.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    contents = ((int(row[0]), row[1], row[2]) for row in reader)
    cursor.executemany('INSERT INTO movies (id, title, genre) VALUES (?, ?, ?)', contents)

with open('data/links.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    contents = ((int(row[0]), row[1], row[2]) for row in reader)
    cursor.executemany('INSERT INTO links (movieId, imbId, tmbId) VALUES (?, ?, ?)', contents)

with open('data/tags.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    contents = ((int(row[0]), row[1], row[2], row[3]) for row in reader)
    cursor.executemany('INSERT INTO tags (userId, movieId, tag, timestamp) VALUES (?, ?, ?, ?)', contents)

with open('data/ratings.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    contents = ((int(row[0]), row[1], row[2], row[3]) for row in reader)
    cursor.executemany('INSERT INTO reviews (users_id, movies_id, rates, timestamp) VALUES (?, ?, ?, ?)', contents)

conn.commit()

def insert_users(firstname, lastname, email, age):
    cursor.execute('''INSERT INTO students (firstname, lastname, email, age)
                        VALUES (?, ?, ?, ?)''', (firstname, lastname, email, age))
    conn.commit()

def insert_actors(firstname, lastname, entertainment):
    cursor.execute('''INSERT INTO advisors (firstname, lastname, entertainment)
                        VALUES (?, ?)''', (firstname, lastname, entertainment))
    conn.commit()

def insert_movies(title, mpa_rating, director, length, released_date, production_company, country):
    cursor.execute('''INSERT INTO clubs (title, mpa_rating, director, length, released_date, production_company, country)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', (title, mpa_rating, director, length, released_date, production_company, country))
    conn.commit()

def insert_reviews(rates, description, movies_id):
    cursor.execute('''INSERT INTO events (rates, description, movies_id)
                        VALUES (?, ?, ?)''', (rates, description, movies_id))
    conn.commit()

def insert_actors_movies(actors_id, movies_id):
    cursor.execute('''INSERT INTO actors_movies (actors_id, movies_id)
                    VALUES (?, ?)''', (actors_id, movies_id))
    conn.commit()

def insert_users_reviews(users_id, reviews_id):
    cursor.execute('''INSERT INTO users_reviews (users_id, reviews_id)
                    VALUES (?, ?)''', (users_id, reviews_id))
    conn.commit()

def insert_movies_reviews(movies_id, reviews_id):
    cursor.execute('''INSERT INTO movies_reviews (movies_id, reviews_id)
                    VALUES (?, ?)''', (movies_id, reviews_id))
    conn.commit()