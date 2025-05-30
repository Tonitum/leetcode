package com.tonitum;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestConsecutive(int[] nums) {
        // put all of the elements into a hashtable
        Map<Integer, Boolean> unique = new HashMap<Integer, Boolean>();
        for (int num : nums) {
            unique.put(num, false);
        }
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            int prev = curr - 1;
            if (unique.get(curr) || unique.containsKey(prev)) {
                continue;
            }
            int currentMax = 1;
            unique.put(curr, true);
            int next = curr + 1;
            while (unique.containsKey(next)) {
                currentMax += 1;
                unique.put(next, true);
                curr = next;
                next = next + 1;
                continue;
            }
            if (currentMax > max) {
                max = currentMax;
            }
        }
        return max;
    }
}
