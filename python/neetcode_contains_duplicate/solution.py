class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Intuition is to create a set of the numbers we've seen
        # iterate through the list, adding one element to the set on each
        # iteration. check element is in set, if yes, return true, if no continue
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        # This has time complexity of O(n) and space complexity of O(n)
        # there is probably some fancy math to do this with space complexity
        # that would be smaller, but I don't know it


        return False

