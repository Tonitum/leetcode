from problem933.python.solution import RecentCounter


class TestSolution933:
    def test_case_one(self):
        obj = RecentCounter()
        res1 = obj.ping(1)
        assert res1 == 1
        res2 = obj.ping(100)
        assert res2 == 2
        res3 = obj.ping(3001)
        assert res3 == 3
        res4 = obj.ping(3002)
        assert res4 == 3
