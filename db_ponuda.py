import sqlite3

conn = sqlite3.connect('filmovi_popis.db')

c = conn.cursor()

#c.execute("""CREATE TABLE filmovi (
       # naziv text,
       # zanr text,
       # broj mjesta integer
       # )""")
#c.execute("INSERT INTO filmovi VALUES ('Osvetnici: Rat beskonacnosti', 'Akcija', '45' )")

c.execute("SELECT * FROM filmovi WHERE zanr = 'Akcija'")
print(c.fetchall())


conn.commit()

conn.close()