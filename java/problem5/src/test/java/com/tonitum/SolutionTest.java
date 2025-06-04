package com.tonitum;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {

    @Test
    public void testCaseOne() {
        String input = "babad";
        Solution handle = new Solution();
        assertEquals("bab", handle.longestPalindrome(input));
    }

    @Test
    public void testCaseTwo() {
        String input = "cbbd";
        Solution handle = new Solution();
        assertEquals("bb", handle.longestPalindrome(input));
    }

}
