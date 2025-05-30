package com.tonitum;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int start = 0;
        Set<Character> substring = new HashSet<Character>();
        int currentMax = 0;
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (!substring.contains(curr)) {
                currentMax += 1;
                substring.add(curr);
                if (max < currentMax) {
                    max = currentMax;
                }
                continue;
            }
            while (substring.contains(curr)) {
                char startCurr = s.charAt(start);
                start += 1;
                substring.remove(startCurr);
                currentMax -= 1;
            }
        }
        return max;
    }
}
