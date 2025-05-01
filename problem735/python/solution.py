class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # TODO: Change this to use a single stack, no need for two
        stack: list[int] = []

        for i in range(len(asteroids)):
            asteroid = asteroids[i]
            if len(stack) == 0:
                stack.append(asteroid)
                continue
            prev_asteroid = stack.pop()
            while True:
                if (prev_asteroid * asteroid) > 0 or (prev_asteroid < 0 and asteroid > 0):
                    stack.append(prev_asteroid)
                    stack.append(asteroid)
                    break
                if abs(prev_asteroid) < abs(asteroid):
                    if len(stack) == 0:
                        stack.append(asteroid)
                        break
                    prev_asteroid = stack.pop()
                    continue
                if abs(prev_asteroid) == abs(asteroid):
                    break
                stack.append(prev_asteroid)
                break
        return stack
        
