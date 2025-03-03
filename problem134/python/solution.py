# two pointers
# one at starting point
# one at ending point
# iterate forward, checking that we can make it to each next gas station
# if we don't have enough gas to travel from ending point to next station,
# increment the starting point back by one, calculate the difference in gas
# add it to our tank and see if we can make the hop.
# if we get to the point where the starting point is before or equal to the ending point,
# return the starting point.
# Otherwise, return -1


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start_ptr = 0
        curr = 0
        trip_length = 0
        gas_tank = 0
        tried_count = 0

        while True:
            if trip_length == len(gas):
                break
            cost_to_next = cost[curr]
            total_gas = gas[curr] + gas_tank
            if total_gas >= cost_to_next:
                curr = curr + 1 if curr + 1 < len(gas) else 0
                gas_tank = total_gas - cost_to_next
                trip_length += 1
                tried_count += 1
                continue

            prev = start_ptr - 1 if start_ptr > 0 else len(gas) - 1
            cost_to_start = cost[prev]
            total_gas = gas[prev] + gas_tank
            if total_gas >= cost_to_start:
                start_ptr = prev
                gas_tank = total_gas - cost_to_start
                trip_length += 1
                tried_count += 1
                continue

            # we need a way to make sure we're trying each node
            if tried_count < len(gas):
                curr = curr + 1 if curr + 1 < len(gas) else 0
                start_ptr = curr
                gas_tank = 0
                trip_length = 0
                tried_count += 1
                continue
            return -1

        return start_ptr
