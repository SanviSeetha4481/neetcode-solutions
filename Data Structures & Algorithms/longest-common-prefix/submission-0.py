class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        res=strs[0]
        for i in strs[0:]:
            while not i.startswith(res):
                res=res[:-1]
            if res=="":
                return ""
        return res
