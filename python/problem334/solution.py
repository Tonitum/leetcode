class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # to find three contiguous increasing numbers, we would iterate forward
        # one index from 1 to n - 1. We would check the forward and backward
        # elements to see if the pattern is ascending.
        # To do this in a non-contiguous fashion, we need to iterate forward 
        # one index (i) from 1 to n - 1. We will track 2 points. First, we will
        # track the lowest point that we've seen that is at most i-1 in the array.
        # Next we will track the i that is higher than our lowest point at i-1.
        # if we find a single point that is greater than that second point, while
        # still keeping low < med, we return true.
        if len(nums) < 3:
            # if there are fewer than 3 elements, the answer is always false
            return False

        # initialize our medium point and the lowest point
        low = nums[0]
        med = nums[1]

        for i in range(2, len(nums)):
            curr = nums[i]
            prev = nums[i - 1]
            # peek forward one index, to see if we have a winner
            if low < med < curr:
                return True

            # if the first two numbers resulted in med <= low, the we want
            # to iterate these two forward
            if med <= low:
                low = prev
                med = curr
                continue

            if not curr <= med:
                continue
            if curr > low or curr > prev:
                med = curr
                if low > prev:
                    low = prev

        return False
