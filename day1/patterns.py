# Pattern-1: Rectangular Star Pattern
n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

# Pattern-2: Right-Angled Triangle Pattern

n = int(input())
for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

# Pattern - 3: Right-Angled Number Pyramid

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Pattern - 4: Right-Angled Number Pyramid - II

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
          print(i,end= " ")
    print()

# Pattern-5: Inverted Right Pyramid

n = int(input())
for i in range(n):
    for j in range(n,i,-1):
        print("*",end=" ")
    print()

# Pattern - 6: Inverted Numbered Right Pyramid

n = int(input())
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(n-j+1,end=" ")
    print()

# Pattern - 7: Star Pyramid

n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end= "")
    for j in range(2*i+1):
        print("*",end="")
    for j in range(n-i-1):
        print(" ",end="")
    print()


