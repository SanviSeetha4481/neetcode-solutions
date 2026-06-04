class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_map=Counter(nums)
        res=[]
        for key in count_map:
            if count_map[key]>len(nums)//3:
                res.append(key)
        return res