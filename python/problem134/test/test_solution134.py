from problem134.python.solution import Solution


class TestSolution134:
    def test_case_one(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]

        res = Solution().canCompleteCircuit(gas, cost)
        assert res == 3

    def test_case_two(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]

        res = Solution().canCompleteCircuit(gas, cost)
        assert res == -1

    def test_case_three(self):
        gas = [2, 3, 1]
        cost = [3, 1, 2]

        res = Solution().canCompleteCircuit(gas, cost)
        assert res == 1
