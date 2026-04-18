class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        return "".join(l)==("".join(l[::-1]))
            
