# Pattern - 8: Inverted Star Pyramid
class solution:
    def print8(n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for j in range(2*n-(2*i+1)):
                print("*",end="")
            for j in range(i):
                print(" ",end="")
            print()

# Pattern - 9: Diamond Star Pattern
    def print9(n):
        for i in range(n):
            print(" "*(n-i-1),end="")
            print("*"*(2*i+1),end="")
            print(" " * (n-i-1))
        for i in range(n):
            print(" "*i,end="")
            print("*"*(2*n-(2*i+1)),end="")
            print(" " * i)

# Pattern - 10: Half Diamond Star Pattern
    def print10(n):
        for i in range(1,n+1):
            print("*" * i)
        for i in range(n-1,0,-1):
            print("*" * i)
    
# Pattern - 11: Binary Number Triangle Pattern
    def print11(n):
        for i in range(n):
            if i%2 == 0:
                start = 1
            else:   
                start = 0
            for j in range(i+1):
                print(start,end="")
                start = 1-start
            print()
solution.print11(6)