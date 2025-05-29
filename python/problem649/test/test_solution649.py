from problem649.python.solution import Solution


class TestSolution649:
    def test_case_one(self):
        senate = "RD"
        assert Solution().predictPartyVictory(senate) == "Radiant"

    def test_case_two(self):
        senate = "RDD"
        assert Solution().predictPartyVictory(senate) == "Dire"

    def test_case_three(self):
        # in this case, in the initial insert, I can only insert one R into 
        # the queue, because there are two Dires ahead
        # so,
        # D
        # DD
        # DDR(x)
        # DDR(x)R(x)
        # DDR(x)R(x)R
        # DDR
        # after that, it's clear that dire wins
        # so, what do I learn from this?
        # I should create a queue of tuples, and walk the tuple list forward 
        # marking the voted param true if the member has voted in this round
        # reset each item after each round
        # if all members are the same party, exit and return
        senate = "DDRRR"
        assert Solution().predictPartyVictory(senate) == "Dire"

    def test_case_four(self):
        senate = "DDRRRR"
        assert Solution().predictPartyVictory(senate) == "Radiant"
