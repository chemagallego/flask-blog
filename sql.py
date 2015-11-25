# sql.py - Model

import sqlite3

with sqlite3.connect('blog.db') as connection:
    c = connection.cursor()

    c.execute('CREATE TABLE posts (title TEXT, post TEXT)')

    c.executescript("""
                    INSERT INTO posts VALUES('Good', 'This is good');
                    INSERT INTO posts VALUES('Well', 'This is well');
                    INSERT INTO posts VALUES('Excellent', 'This is excellent');
                    INSERT INTO posts VALUES('Good', 'This is okay');
                    """)

    
    
