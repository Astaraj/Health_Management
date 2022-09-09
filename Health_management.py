# Health Management System
# 3 clients - Harry, Rohan and Hammad
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input("Enter 1 for excersise and 2 for food: "))
        if (c == 1):
            value = input("Type here:\n")
            with open("harry_ex.txt", "a") as op:
                op.write(str(getdate()) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("harry_food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif (k == 2):
        c = int(input("Enter 1 for excersise and 2 for food: "))
        if (c == 1):
            value = input("Type here\n")
            with open("Debendra_ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("Debendra_food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif (k == 3):
        c = int(input("Enter 1 for excersise and 2 for food: "))
        if (c == 1):
            value = input("Type here\n")
            with open("Asit_ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("Asit_food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        else:
            print("Please enter valid input.")
    else:
        print("Please enter valid input.")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for excersise and 2 for food: "))
        if (c == 1):
            with open("harry_ex.txt") as op:
                for i in op:
                    print(i, end = "")
        elif (c == 2):
            with open("harry_food.txt") as op:
                for i in op:
                    print(i, end = "")
    elif (k == 2):
        c = int(input("Enter 1 for excersise and 2 for food: "))
        if (c == 1):
            with open("Debendra_ex.txt") as op:
                for i in op:
                    print(i, end = "")
        elif (c == 2):
            with open("Debendra_food.txt") as op:
                for i in op:
                    print(i, end = "")
    elif (k == 3):
        c = int(input("Enter 1 for excersise and 2 for food: "))
        if (c == 1):
            with open("Asit_ex.txt") as op:
                for i in op:
                    print(i, end = "")
        elif (c == 2):
            with open("Asit_food.txt") as op:
                for i in op:
                    print(i, end = "")
    else:
        print("Please enter valid input.")

print("Health Management System: ")
a = int(input("Press 1 for log the value and 2 for retrieve: "))

if a == 1:
    b = int(input("Press 1 for Harry,\n2 for Debendra,\n3 for Asit: "))
    take(b)
elif a == 2:
    b = int(input("Press 1 for Harry,\n2 for Debendra,\n3 for Asit: "))
    retrieve(b)
else:
    print("Please enter valid input.")

