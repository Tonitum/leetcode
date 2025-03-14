class Solution:
    def maxArea(self, height: list[int]) -> int:
        start: int = 0
        end: int = len(height) - 1
        max_area = min(height[start], height[end]) * (end - start)

        for _ in range(len(height) - 1):
            # move the smaller side
            if height[start] <= height[end]:
                start = start + 1
            else:
                end = end - 1
            area = min(height[start], height[end]) * (end - start)
            if area > max_area:
                max_area = area

        return max_area
