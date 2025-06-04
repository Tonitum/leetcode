package com.tonitum;

class Solution {
    public String longestPalindrome(String s) {
        // dynamic programming approach
        int n = s.length();
        // our longest will start as the first character
        int start = 0;
        int end = 0;
        // track a list of existing palindromes in the string
        boolean[][] dp = new boolean[n][n];
        // check for palindromes of length len at each i
        for (int len = 0; len < n; len++) {
            // i is our left pointer
            for (int i = 0; i + len < n; i++) {
                // if the first and last character of this len string
                // are equal, then this could be a palindrome
                boolean edgesEqual = s.charAt(i) == s.charAt(i + len);
                // if the length of the palindrome is 0 or 1, then there is no
                // middle and we can know that if the edges were equal, this is 
                // definitely a palindrome. Otherwise, if the two inner characters
                // are a palindrome, we know this is a larger palindrome
                dp[i][i + len] =  edgesEqual && (len < 2 || dp[i + 1][i + len - 1]);
                // if this position is a palindrome, and if the len of this position
                // is larger than the current largest palindrome, update the start/end.
                if (dp[i][i + len] && len > end - start) {
                    start = i;
                    end = i + len;
                }
            }
        }
        // return the substring at from start to end + 1
        return s.substring(start, end + 1);
    }
}
