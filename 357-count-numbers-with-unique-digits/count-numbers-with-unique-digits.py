class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if(n==0):
            return 1
        count=10
        avail=9
        unique=9
        for i in range(2,n+1):
            unique*=avail
            count+=unique
            avail-=1
        return count
