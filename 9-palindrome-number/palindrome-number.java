class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;
        if(x==0) return true;
        if(x%10==0) return false;

        int originalx=x;
        int numrev=0;
        while (x>0){
        int lastdigit=x%10;
        numrev=numrev*10+lastdigit;
        x=x/10;
        }return numrev==originalx;
    }
}