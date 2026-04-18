class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start=0
        end=len(heights)-1
        max_amount=0
        while start<end:
            area=abs(end-start)*(min(heights[end],heights[start]))
            max_amount=max(max_amount,area)
            if heights[end]>heights[start]:
                start+=1
            else:
                end-=1
        return max_amount
