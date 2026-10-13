class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup=set(nums)
        l=0
        for n in lookup:
            if (n-1) not in lookup:
                length=1
                while (n+length) in lookup:
                    length+=1
                l=max(length,l)
        return l



