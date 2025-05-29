from problem735.python.solution import Solution


class TestSolution735:
    def test_case_one(self):
        asteroids = [5, 10, -5]
        assert Solution().asteroidCollision(asteroids) == [5, 10]

    def test_case_two(self):
        asteroids = [5, -10, -5]
        assert Solution().asteroidCollision(asteroids) == [-10, -5]

    def test_case_three(self):
        asteroids = [8, -8]
        assert Solution().asteroidCollision(asteroids) == []

    def test_case_four(self):
        asteroids = [10, 2, -5]
        assert Solution().asteroidCollision(asteroids) == [10]

    def test_case_five(self):
        asteroids = [-2, -1, 1, 2]
        assert Solution().asteroidCollision(asteroids) == [-2, -1, 1, 2]

    def test_case_six(self):
        asteroids = [-2,-2,1,-2]
        assert Solution().asteroidCollision(asteroids) == [-2,-2,-2]
