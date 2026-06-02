class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        first=0
        last=len(nums)-1
        while first<last:
            if nums[first]==val and nums[last]!=val:
                nums[first],nums[last]=nums[last],nums[first]
                first+=1
                last-=1
            elif nums[last]==val:
                last-=1
            elif nums[first]!=val:
                first+=1
        for i in nums:
            if i!=val:
                count+=1
        return count

        