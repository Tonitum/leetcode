class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        int prev = nums[0];
        result[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            result[i] = prev;
            prev = nums[i] * prev;

        }
        prev = nums[nums.length - 1];

        for (int i = nums.length - 2; i >= 0; i--) {
            result[i] = prev * result[i];
            prev = nums[i] * prev;
        }
        return result;
    }
}
