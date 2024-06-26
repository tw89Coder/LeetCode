class Solution {
    public boolean isPalindrome(int x) {        
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }

        long temp = x;
        long reversed = 0;

        while (temp != 0) { 
            reversed = reversed * 10 + temp % 10; 
            temp /= 10;
        }

        return(x == reversed);
    }
}