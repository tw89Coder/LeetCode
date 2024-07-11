class Solution {
    public int myAtoi(String s) {
        int index = 0, sign = 1, total = 0;
        int length = s.length();

        // Step 1: Remove Whitespaces
        while (index < length && s.charAt(index) == ' ') {
            index++;
        }

        // Step 2: Handle Signs
        if (index < length && (s.charAt(index) == '+' || s.charAt(index) == '-')) {
            sign = (s.charAt(index) == '-') ? -1 : 1;
            index++;
        }

        // Step 3: Convert number and avoid overflow
        while (index < length) {
            // Convert the character at the current index to its corresponding integer value
            int digit = s.charAt(index) - '0';
            if (digit < 0 || digit > 9) {
                break;
            }

            // Check if total will be overflow after 10 times and add digit
            if (total > (Integer.MAX_VALUE - digit) / 10) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            total = total * 10 + digit;
            index++;
        }

        return total * sign;
    }
}
