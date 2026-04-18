class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in range(len(nums)):
            difference=target-nums[i]
            if difference not in s:
                s[nums[i]]=i
            else:
                return ([s[difference],i])
