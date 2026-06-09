class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        temp=0
        length=float('inf')
        for right in range(len(nums)):
            temp+=nums[right]
            while temp>=target:
                length=min(length,(right-left+1))
                temp-=nums[left]
                left+=1
        return 0 if length==float('inf') else length
        

