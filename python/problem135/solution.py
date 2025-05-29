class Solution:
    def candy1(self, ratings: list[int]) -> int:
        # we will always have at least 1 candy for each child in the list
        candy_count = len(ratings)

        if len(ratings) == 0:
            return 0

        if len(ratings) == 1:
            return 1

        peak_rating = ratings[0]
        peak_idx = 0
        valley_idx = 0
        peak_height = 0
        for i in range(1, len(ratings) - 1):
            curr = ratings[i]
            next = ratings[i+1]
            if curr > peak_rating:
                peak_rating = curr
                peak_idx = i
                peak_height += 1
                candy_count += peak_height
                continue

            if curr > next:
                candy_count += 1
                continue

        return candy_count

    def candy(self, ratings: list[int]) -> int:
        candy_map: list[int] = [1] * len(ratings)
        previous_rating = ratings[0]

        for i in range(1, len(ratings)):
            curr = ratings[i]
            if curr > previous_rating:
                if (candy_map[i] <= candy_map[i-1]):
                    candy_map[i] = candy_map[i-1] + 1
            previous_rating = curr

        for i in range(len(ratings)-1, -1, -1):
            curr = ratings[i]
            if curr > previous_rating:
                if (candy_map[i] <= candy_map[i+1]):
                    candy_map[i] = candy_map[i+1] + 1
            previous_rating = curr
        return sum(candy_map)
