def adult_or_not(age):
    if age >= 18:
        return "adult"
    return "not adult"
age = int(input("enter your age:"))
print(adult_or_not(age))

# if elif else ladder for marks

marks = int(input("enter your marks:"))

if marks >= 90:
    print("A21")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
elif marks >=60 and marks < 70:
    print("D")
elif marks >= 50 and marks < 60:
    print("E")
elif marks < 50:
    print("F")
else:
    print("invalid marks")