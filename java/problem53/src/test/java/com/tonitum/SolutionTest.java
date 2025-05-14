package com.tonitum;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class SolutionTest {

    @Test
    public void testCaseOne() {
        Solution handle = new Solution();
        int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };

        assertEquals(6, handle.maxSubArray(nums));
    }

    @Test
    public void testCaseTwo() {
        Solution handle = new Solution();
        int[] nums = {1};

        assertEquals(1, handle.maxSubArray(nums));
    }

    @Test
    public void testCaseThree() {
        Solution handle = new Solution();
        int[] nums = {5,4,-1,7,8};

        assertEquals(23, handle.maxSubArray(nums));
    }

    @Test
    public void testCaseFour() {
        Solution handle = new Solution();
        int[] nums = {-1};

        assertEquals(-1, handle.maxSubArray(nums));
    }

    @Test
    public void testCaseFive() {
        Solution handle = new Solution();
        int[] nums = {-2, -1};

        assertEquals(-1, handle.maxSubArray(nums));
    }

    @Test
    public void testCaseSix() {
        Solution handle = new Solution();
        int[] nums = {-1,0,-2};

        assertEquals(0, handle.maxSubArray(nums));
    }
}
