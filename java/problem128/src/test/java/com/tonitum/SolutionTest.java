package com.tonitum;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {

    @Test
    public void testCaseOne() {
        int[] nums = { 100, 4, 200, 1, 3, 2 };
        Solution handle = new Solution();
        int res = handle.longestConsecutive(nums);
        assertEquals(4, res);
    }

    @Test
    public void testCaseTwo() {
        int[] nums = { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 };
        Solution handle = new Solution();
        int res = handle.longestConsecutive(nums);
        assertEquals(9, res);
    }

    @Test
    public void testCaseThree() {
        int[] nums = { 1, 0, 1, 2 };
        Solution handle = new Solution();
        int res = handle.longestConsecutive(nums);
        assertEquals(3, res);
    }
}
