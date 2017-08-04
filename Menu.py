import sys
import warnings
import pymysql
from databaseFunc import *

def printOptions():

    print("1: Add item to library")
    print("2: Remove item from library")
    print("3: Search for item in library")
    print("4: Display all items in library")
    print("5: Keyword find")
    print("6: Exit")

def select(choice):
    if choice == 1:
        id = input("What is the ID?: \n")
        name = input("What is the name?: ")
        addItem(id,name)

    elif choice == 2:
        remove(input("What item do you want to remove?: "))

    elif choice == 3:
        if search(input("What item are you searching for?: ")) == True:
            print("Item in Library")
        else:
            print("Item not in Library")

    elif choice == 4:
        displayAll()

    elif choice == 5:
        keyword(input("What keyword?: "))

    elif choice == 6:
        sys.exit(1)
        # cleanup
        cursor.close()
        db.close()



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

