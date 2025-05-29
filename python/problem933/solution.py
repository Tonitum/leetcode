class RecentCounter:

    requests: list[int] = []
    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        recent_requests = 1
        for request in self.requests:
            if request >= (t - 3000):
                recent_requests += 1
                continue
            break
        self.requests.insert(0, (t))
        return recent_requests


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
