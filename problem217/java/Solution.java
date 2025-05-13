import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            if (seen.contains(curr)) {
                return true;
            }
            seen.add(curr);
        }
        return false;
    }
}
