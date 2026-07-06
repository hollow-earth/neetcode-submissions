class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if len(stack) == 0:
                stack.append(a)
            else:
                tmp = a
                if tmp > stack[-1]:
                    stack.append(tmp)
                else:
                    while len(stack) >= 1 and stack[-1] > 0 and tmp < 0: # stack[-1] * a is only negative if the signs are different
                        popped = stack.pop()
                        magnitude = max(abs(tmp), abs(popped))
                        direction = 0 if abs(tmp + popped) == 0 else (tmp + popped) // abs(tmp + popped)
                        tmp = magnitude * direction
                    if tmp != 0: stack.append(tmp)

        return stack