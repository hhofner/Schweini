import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE task
            (date text, title text, due text, time real)''')

c.execute("INSERT INTO task VALUES ('2020-10-29', 'Design Schweini Database', '2020-10-30', 100)")

conn.commit()

conn.close()
