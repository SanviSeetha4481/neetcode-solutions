class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for num in nums:
            if num not in map:
                map[num]=1
            else:
                map[num]+=1
        l=sorted(map,key=map.get,reverse=True)
        return l[:k]
            