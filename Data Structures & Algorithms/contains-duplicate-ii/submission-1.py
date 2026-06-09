class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map={}
        n=len(nums)
        for i in range(n):
            if nums[i] in hash_map:
                if abs(i-(hash_map[(nums[i])]))<=k:
                    return True
                else:
                    hash_map[(nums[i])]=i
            else:
                hash_map[(nums[i])]=i

        return False
