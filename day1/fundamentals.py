# Finding the Length of a String
class Solution:
    def find_length(self,s):
        return len(s)

if __name__ == "__main__":
    obj = Solution()
    s = "Hello, World!"
    print(obj.find_length(s))  # Output: 13

# Accessing Individual Characters
class Solution:
    def access_char(self,s):
        for i in range(len(s)):
            return s[i]
if __name__ == "__main__":
    obj =Solution()
    s = "Hello, World!"
    print(obj.access_char(s))  # Output: H

# Passing, Returning, and Assigning Strings

def modify_string(s):
    new_str = s
    new_str += " Modified"
    return new_str
original = "Original String"
modified = modify_string(original)
print("Original:", original)  # Output: Original String
print("Modified:", modified)  # Output: Original String Modified
