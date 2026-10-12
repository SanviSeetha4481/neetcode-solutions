class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}
        for i in range(0,len(nums)):
            if target-nums[i] in lookup:
                return [(lookup[target-nums[i]]),i]
            else:
                lookup[(nums[i])]=i