import sys
import warnings
import pymysql
from databaseFunc import *

def printOptions():

    print("1: Add item to library")
    print("2: Remove item from library")
    print("3: Search for item in library")
    print("4: Display all items in library")
    print("5: Keyword search")
    print("6: Exit")

def select(choice):
    if choice == 1:
        id = input("What is the ID?: \n")
        name = input("What is the name?: ")
        addItem(id,name)

    if choice == 2:
        remove(input("What item do you want to remove?: "))

    if choice == 3:
        search(input("What item are you searching for?: "))

    if choice == 4:
        displayAll()

    if choice == 5:
        keyword(input("What keyword?: "))

    if choice == 6:
        sys.exit(1)



def main():
    while 1:
        cond = True
        printOptions()
        while cond:
            try:
                choice = int(input("Select an option(1-6): "))
                if choice not in [1, 2, 3, 4, 5, 6]:
                    print("Error, select option 1-6")
                else:
                    cond = False
            except:
                print("Error, select option 1-6")

        print()
        select(choice)
        print()
    return 0

main()

#cleanup
cursor.close()
db.close()