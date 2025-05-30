package com.tonitum;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {

    @Test
    public void testCaseOne() {
        String s = "abcabcbb";
        Solution handle = new Solution();
        assertEquals(3, handle.lengthOfLongestSubstring(s));
    }
    @Test
    public void testCaseTwo() {
        String s = "bbbbb";
        Solution handle = new Solution();
        assertEquals(1, handle.lengthOfLongestSubstring(s));
    }
    @Test
    public void testCaseThree() {
        String s = "pwwkew";
        Solution handle = new Solution();
        assertEquals(3, handle.lengthOfLongestSubstring(s));
    }
}
