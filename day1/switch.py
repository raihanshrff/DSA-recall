# switch statement in Python
day = int(input("Enter a day of the week: "))
switcher ={
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday"
        
    }
if day in switcher:
    print(switcher[day])
else:
    print("Invalid day")


x = 10
y = 20

match x+y:
    case 30:
        print("correct")
    case 40:
        print("incorrect")
    case _:
        print("invalid")