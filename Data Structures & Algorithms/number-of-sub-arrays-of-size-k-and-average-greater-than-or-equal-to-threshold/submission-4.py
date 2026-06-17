class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        curSum=sum(arr[:k-1])
        for l in range(len(arr)-k+1):
            curSum+=arr[l+k-1]
            if curSum/k>=threshold:
                count+=1
            curSum-=arr[l]
        return count