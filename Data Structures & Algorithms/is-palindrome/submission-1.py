class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        answer=""
        while i<len(s):
            if s[i].isalnum():
                answer+=(s[i].lower())
            i+=1
        return answer==answer[::-1]
