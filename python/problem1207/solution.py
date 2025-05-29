class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # convert the list into a dictionary
        counts: dict[int, int] = {}
        for i in arr:
            if i not in counts:
                counts[i] = 1
                continue
            counts[i] += 1

        unique_counts: dict[int, bool] = {}
        for count in counts.values():
            if not unique_counts.get(count, False):
                unique_counts[count] = True
                continue
            return False

        return True
