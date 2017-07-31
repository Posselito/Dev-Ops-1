import pymysql
#requires an already created databasse and table for inventory
#connect to db and prepare cursor
db = pymysql.connect("localhost", "username", "password", "testdb")
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
version = cursor.fetchone()

print("Version: %s" %version)

def addItem(id,name):
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

def fetchAll():
    items = []
    cursor.execute("""SELECT * FROM INVENTORY""")
    data = cursor.fetchall()
    for each in data:
        items.append(each[1])
    return items

def remove(DName):
    try:
        cursor.execute("""DELETE FROM INVENTORY WHERE NAME = %s""", (DName))
        db.commit()
        print("Item removed")
    except:
        ("Item not in library")

def displayAll():
    results = fetchAll()
    for each in results:
        print(each)

def search(QName):
    items = fetchAll()
    for each in items:
        if QName == each:
            i = 1
    if i == 1:
        print("Item in library")
    else:
        print("Item not in library")


def keyword(KName):
    items = fetchAll()
    results = []
    for each in items:
        if KName in each:
            results.append(each)
    for each in results:
        print(each)
    if results == None:
        print("No results")