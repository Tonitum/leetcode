import math


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # naive approach is to iterate through the list forward
        # for each element, iterate forward to see if the delta is in the list
        # if it is, then remove the delta element from the list.
        # this is o(n^2) runtime, o(1) runtime

        operation_count = 0

        # Iterate through the nums list once to count the number of unique numbers
        # and how many times they occur
        counts: dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
                continue
            counts[nums[i]] += 1

        # iterate through the number counts, and check for the appropriate pair
        # number.
        for key in counts.keys():
            value = counts[key]
            if key == k / 2:
                operation_count += math.floor(value / 2)
                continue

            diff = k - key
            if diff not in counts:
                continue
            diff_count = counts[diff]
            operation_count += min(value, diff_count)
            counts[key] = 0

        return operation_count
