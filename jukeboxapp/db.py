import sqlite3
from sqlite3 import ...


# TO DO: create a sqlite3 database (data.db)

#path = '/Users/marinelafargue/Desktop/movie_app/database.py'
#conn = sqlite3.connect(path)

# TO DO: each function below has to execute a SQL query and return the result (movies) if there's one.
def create_tables()
  curs.execute('''CREATE TABLE IF NOT EXISTS musics (
  id  INTEGER  AUTOINCREMENT,
  title TEXT,
  release_timestamp REAL,
  watched INTEGER)'''
);
  conn.()


def add_music(title, release_timestamp)
  curs.execute('''INSERT INTO musics (title, release_timestamp, watched) VALUES (?, ?, 0)''', (title,release_timestamp))

  conn.() #Ne pas oublier de valider les modifications



def get_music()
  curs.execute('''SELECT *, FROM musics''');

   curs.fetchall()




def mark_music_as_pref(title)
  .execute('''UPDATE musics SET watched = 1 WHERE title = (?)''',(title))
  conn.()

def get_pref_music():
  .execute('''SELECT * FROM musics WHERE watched = 1 ''')
   curs.fetchall()
  conn.()
