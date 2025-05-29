class Solution:
    RADIANT: str = "R"
    DIRE: str = "D"

    def predictPartyVictory(self, senate: str) -> str:
        senators: list[str] = [c for c in senate]

        while len(senators) > 1:
            front = senators.pop(0)
            voted = False
            for i in range(len(senators)):
                senator = senators[i]
                if senator != front:
                    senators.pop(i)
                    voted = True
                    break
            if not voted:
                break
            senators.append(front)

        if senators[0] == self.DIRE:
            return "Dire"
        else:
            return "Radiant"
