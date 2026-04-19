class Solution:
    def isValid(self, s: str) -> bool:
        dict={')':'(','}':'{',']':'['}
        if len(s)==0:
            return True
        l='({['
        stk=[]
        for i in s:
            if i in l:
                stk.append(i)
            else:
                if not stk or stk.pop()!=dict[i]:
                    return False
                    
        if len(stk)==0:
            return True
        else:
            return False