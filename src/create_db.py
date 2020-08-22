import sqlite3
conn = sqlite3.connect('database.db')
print "Opened database successfully"
conn.execute('CREATE TABLE history(RemoteServer TEXT, LowRange TEXT, HighRange TEXT)')
print "Successfully created history table in database"
conn.close()
