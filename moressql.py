import sqlite3

conn = sqlite3.connect('test1.db')

#Cursor allows users to interact with the database
c = conn.cursor()

def printTbl(curs):
	result = curs.execute("SELECT ROWID, firstName FROM people")
	for r in result:
		print(str(r[0]) + ") "+str(r[1]))
printTbl(c)
done = False
while not done:
	idd = int(input("Enter Desired ID: "))

	choice = str(input("What would you like to do? View, Delete, or Update? "))

	if choice == "View" or choice == "view":
		result = c.execute("SELECT * FROM people WHERE ROWID = "+str(idd))
		for r in result:
			print("First Name: "+r[0])
			print("Last Name: "+r[1])
			if r[2]:
				print("Age: "+r[2])
			else:
				print("Age: Null")
	elif choice == "Delete" or choice =="delete":
		c.execute("DELETE FROM people WHERE ROWID = "+str(idd))
		print("Deletion Successful")
		conn.commit()
	elif choice == "Update" or choice == "update":
		result = c.execute("SELECT * FROM people WHERE ROWID = "+str(idd))
		for r in result:
			sheesh = input("FirstName["+r[0]+"]: ")
			if(sheesh != ""):
				c.execute("UPDATE people SET firstName = \""+sheesh+"\" WHERE ROWID = "+str(idd))
			sheesh = input("LastName["+r[1]+"]: ")
			if(sheesh != ""):
				c.execute("UPDATE people SET lastName = \""+sheesh+"\" WHERE ROWID = "+str(idd))
			if(r[2]):
				sheesh = input("Age["+r[2]+"]: ")
			else:
				sheesh = input("Age[Null]: ")
			if(sheesh != ""):
				c.execute("UPDATE people SET age = \""+sheesh+"\" WHERE ROWID = "+str(idd))
			conn.commit()
	print("Updated Table: ")
	printTbl(c)
	choice = input("You done? (y/n) ")
	if(choice == "y" or choice =="Y"):
		done = True
	elif(choice == "n" or choice == "N"):
		done = False
	else:
		print("Error, relooping")

