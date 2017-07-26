import pymysql
#requires an already created databasse and table for inventory
#connect to db and prepare cursor
db = pymysql.connect("localhost", "username", "password", "testdb")
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

print("Version: %s" %data)
#add new inventory item
'''
id = input("Enter ID number: ")
name = input("Enter product name: ")
try:
    #input inventory data
    cursor.execute("""INSERT INTO INVENTORY VALUES (%s, %s)""", (id, name))
    #commit to db
    db.commit()
    print("Success!")
except:
    #rollback incase any error
    print("Error")
    db.rollback()
'''
#end
#search for item
QName = input("What item are you searching for?: ")

try:
    cursor.execute("""SELECT * FROM INVENTORY WHERE NAME = %s""", (QName))
    data = cursor.fetchone()
    if data[1] == QName:
        print("Item in library")
except:
    print("Item not in Library")
#end
db.close()