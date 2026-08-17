class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt=0
        res=[]
        for i in s:
            if i=='(':
                res.append(i)
                cnt+=1
            elif i==')' and cnt>0:
                res.append(i)
                cnt-=1
            elif i!= ')':
                res.append(i)
        filtered=[]
        for i in res[::-1]:
            if i=='(' and cnt>0:
                cnt-=1
            else:
                filtered.append(i)
        return "".join(filtered[::-1])

