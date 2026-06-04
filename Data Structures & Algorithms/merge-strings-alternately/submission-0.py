class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        res=""
        mini=""
        maxi=""
        if len(word1)<len(word2):
            mini=word1
            maxi=word2
        else:
            mini=word2
            maxi=word1

        while i<len(mini):
            res+=word1[i]
            res+=word2[i]
            i+=1
        res+=maxi[i:]
        
        return res

