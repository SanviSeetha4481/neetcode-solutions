class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]=1+count.get(n,0)
        for c,f in count.items():
            freq[f].append(c)
        
        res=[]
        for parse in range(len(freq)-1,0,-1):
            for num in freq[parse]:
                res.append(num)
                if len(res)==k:
                    return res

