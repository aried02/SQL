import sqlite3

#Connect to the database
conn = sqlite3.connect('test1.db')

#Cursor allows users to interact with the database
c = conn.cursor()
#The cursor has an execute method used to run queries
c.execute("INSERT INTO people(firstName, lastName, age) VALUES (?,?,?)", ("Tim", "Red", 33))

#The connection's commit method must be invoked to 'save' the effects of the commans
conn.commit()

#Execute a SELECT statement
result = c.execute("SELECT * FROM people")

#For each row
for r in result:
	#For each column in the row
	for j in r:
		print(str(j) + " : ", end="")
	print()

conn.close()


