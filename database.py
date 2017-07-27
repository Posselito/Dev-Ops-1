import pymysql
#requires an already created databasse and table for inventory
#connect to db and prepare cursor
db = pymysql.connect("localhost", "username", "password", "testdb")
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
version = cursor.fetchone()

print("Version: %s" %version)
def addItem():

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

def search():
    QName = input("What item are you searching for?: ")

    try:
        cursor.execute("""SELECT * FROM INVENTORY WHERE NAME = %s""", (QName))
        result = cursor.fetchone()
        if result[1] == QName:
            print("Item in library")
    except:
        print("Item not in Library")

def displayAll():
    cursor.execute("""SELECT * FROM INVENTORY""")
    data = cursor.fetchall()
    for each in data:
        print(each[1])

def remove():
    DName = input("What item do you want to remove?: ")
    try:
        cursor.execute("""DELETE FROM INVENTORY WHERE NAME = %s""", (DName))
        db.commit()
        print("Item removed")
    except:
        ("Item not in library")

#cleanup
cursor.close()
db.close()