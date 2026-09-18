class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        if not b:
            return 1
        Mod=1337
        def power(x,n):
            ans=1
            while n>0:
                if n%2==1:
                    ans=(ans*x) % 1337
                    n=n-1
                else:
                    n=n//2 
                    x=(x*x)%1337
            return ans
        ans=1
        for digit in b:
            ans=power(ans,10)
            ans=(ans*power(a,digit))%1337
        return ans


