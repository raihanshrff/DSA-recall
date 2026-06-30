import math
class solution:
    # Count digits in a number
    def countdigits(n):
        count = 0
        while n > 0:
            count +=1
            n //= 10
        return count
    
    # Reverse Digits of A Number
    def rev(n):
        rev = 0
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        return rev
    
    # Check if a number is Palindrome or Not
    def palindrome(n):
        og = n
        rev = 0
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        return og == rev
    
    # Check if a number is Armstrong Number or not
    def armstrong(n):
        og = n
        add = 0
        while n > 0:
            digit = n % 10
            add = add + (digit*digit*digit)
            n //= 10
        return og == add

    # print all divisors
    def divisors(n):
        # res =[]    TC: O(N)
        # for i in range(1,n):
        #     if n % i == 0:
        #         res.append(i)
        # return res
        # TC  : O(1)
        res = []
        for i in range(1,int(math.isqrt(n))+1):
            if n % i == 0:
                res.append(i)
                if i != n//i:
                    res.append(n//i)
        return sorted(res)
    # check prime
    def prime(n):
        count = 0
        for i in range(1,n+1):
            if n % i == 0 :
                count +=1
        return count == 2
    # finding gcd
    def gcd(n1,n2):
        # gcd = 1 TC : O(min(n1,n2))
        # for i in range(1,min(n1,n2)+1):
        #     if n1 % i == 0 and n2 % i == 0 :
        #         gcd = i
        # return gcd
        for i in range(min(n1,n2),0,-1):
            if n1 % i == 0 and n2 % i == 0 :
                return i
        return 1


print(solution.gcd(20,40))