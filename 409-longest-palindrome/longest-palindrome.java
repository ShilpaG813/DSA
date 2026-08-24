class Solution {
    public int longestPalindrome(String s) {
        int count[]=new int[128];
        for(char c:s.toCharArray()){
            count[c]++;
        }
        boolean odd=false;
        int len=0;
        for(int n:count){
            if(n%2==0){
                len+=n;
            }else{
                len+=n-1;
                odd=true;
            }
        }
        if(odd){
            len++;
        }return len;
    }
}