@staticmethod
class Solution:
    # print names N times using backtrack
    def printNames(self,i,n):
        if i > n:
            return
        print("raihan")
        self.printNames(i+1,n)
    # print 1 - n
    def printNames(self,i,n):
        if i > n:
            return
        print(i)
        self.printNames(i+1,n)
    # print n
    def printNames(self,i):
        if i<1:
            return
        print(i)
        self.printNames(i-1)
    def p(self,i):
        if i < 1:
            return
        print(i)
        self.p(i-1)
        
    

# obj = Solution()
# obj.p(5)
# obj.printNames(5) 

class solution:
    def sumdig(self,n):
        add = 0
        for i in range(1,n+1):
            add += i
        print(add)
    # recursive func
    def sumofn(self,n):
        if n ==1:
            return 1
        return n + self.sumofn(n-1)
    def mul(self,n):
        res = 1
        for i in range(1,n+1):
            res *= i
        print(res)
    def fact(n):
        if n == 0:
            return 1
        return n * fact(n-1)
        

    
# obj = solution()
# print(obj.fact(5))
# print(obj.sumofn(5))

def fact(n):
        if n == 0:
            return 1
        return n * fact(n-1)
# print(fact(5))

# reverse an array
# brute force
n = int(input())
arr = list(map(int,input().split(",")))

arr1 = [0] * n
for i in range(len(arr)):
    arr1[i] = arr[n-1-i]
print(arr1)

# two pointer
left = 0
right = len(arr)-1
while left < right :
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1
print(arr)
# single pointer 
class Solution:
    def rev(self,arr,i):
        n = len(arr)
        if i >= n//2:
            return
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
        self.rev(arr,i+1)
obj=Solution()
arr = [1,2,3,4,5]
obj.rev(arr,0)
print(arr)
# check string in palindrome
class Solution:
    def palindrome(self,s,i):
        n = len(s)
        if i >= n//2:
            return True
        if s[i]!=s[n-i-1]:
            return False
        return self.palindrome(s,i+1)
obj = Solution()
s = "madam"
print(obj.palindrome(s,0))
# normal approach
s = "madamsefb"
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print(True)
else:
    print(False)

# fibonacci through rescursion
class Solution:
    def fibonacci(self,n):
        if n <= 1:
            return n
        last = self.fibonacci(n-1)
        slast = self.fibonacci(n-2)
        return last + slast

obj = Solution()
print(obj.fibonacci(4))


