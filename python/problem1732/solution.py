class Solution():
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = 0
        curr_altitude = 0
        for diff in gain:
            curr_altitude += diff
            if curr_altitude > max_altitude:
                max_altitude = curr_altitude

        return max_altitude
