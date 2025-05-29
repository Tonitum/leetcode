class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count = -1 
        for start in range(len(blocks) - k + 1):
            end = start + k - 1
            block_slice = blocks[start:end+1]
            b_count = block_slice.count("B")
            if b_count >= k:
                return 0
            if k - b_count < min_count:
                min_count = k - b_count
                continue
            if min_count == -1:
                min_count = k - b_count
        return min_count
