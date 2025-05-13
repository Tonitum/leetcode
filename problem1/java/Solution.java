import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();
        seen.put(nums[0], 0);

        for ( int i = 1; i < nums.length; i++) {
            int curr = nums[i];
            int diff = target - curr;
            if (seen.containsKey(diff))  {
                seen.put(curr,i);
                continue;
            }
            return new int[]{seen.get(diff), i};
        }
        return new int[]{-1,-1};
    }
}

