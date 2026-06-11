class Solution:
    def trap(self, height: List[int]) -> int:
        l_max=height[0]
        r_max=height[(len(height)-1)]
        l=0
        water_trapped=0
        r=len(height)-1
        while l<r:
            if height[l]<l_max:
                water_trapped+=l_max-height[l]
            else:
                l_max=height[l]
            if height[r]<r_max:
                water_trapped+=r_max-height[r]
            else:
                r_max=height[r]
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return water_trapped
