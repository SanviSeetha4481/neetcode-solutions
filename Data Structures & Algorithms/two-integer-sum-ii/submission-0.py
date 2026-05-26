class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapp={}
        for i in range(len(numbers)):
            if target-numbers[i] not in mapp:
                mapp[numbers[i]]=i
            else:
                complement=mapp[target-(numbers[i])]
                return [complement+1,i+1]