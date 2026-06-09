class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        left=0
        right=k
        while left<=(len(nums)-k):
            ans.append((max(nums[left:right])))
            right+=1
            left+=1
        return ans

