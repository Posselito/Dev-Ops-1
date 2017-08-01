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
    i = 0
    for each in results:
        print(each)
        i += 1
    return i

def search(QName):
    items = fetchAll()
    for each in items:
        if QName == each:
            return True


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
    return results