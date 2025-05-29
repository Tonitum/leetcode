class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # o(1) space
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if major == nums[i]:
                count += 1
                continue
            elif count == 0:
                major = nums[i]
                count += 1
            else:
                count -= 1

        return major


    def majorityElement2(self, nums: list[int]) -> int:
        # create a hash map
        # linear time
        num_counts: dict[str, int] = {}

        for num in nums:
            num_counts[str(num)] = num_counts[str(num)] + 1 if str(num) in num_counts else 1

        greatest_key: str = "-1" 
        greatest_value: int = -1

        for key, value in num_counts.items():
            if value > greatest_value:
                greatest_key = key
                greatest_value = value

        return int(greatest_key)
