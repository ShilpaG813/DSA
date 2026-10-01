class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        res=[-1]*n
        stk=[]
        for i in range(2*n-1,-1,-1):
            idx=i%n
            while stk and nums[stk[-1]]<=nums[idx]:
                stk.pop()
            if stk:
                res[idx]=nums[stk[-1]]
            stk.append(idx)
        return res
        