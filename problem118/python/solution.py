class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        output: list[list[int]] = []
        for i in range(numRows):
            output.insert(i, [1])
            if len(output[i]) - 1 == i:
                continue
            output[i].append(1)
            if len(output[i]) - 1 == i:
                continue
            for j in range(1, i):
                output[i].insert(
                    len(output[i]) - 1, output[i - 1][j] + output[i - 1][j - 1]
                )
        return output
