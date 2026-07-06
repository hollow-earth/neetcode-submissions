class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            _tmp = a
            while stack and _tmp < 0 and stack[-1] > 0:
                diff = stack[-1] + _tmp
                if diff > 0:
                    _tmp = 0
                elif diff < 0:
                    stack.pop()
                else:
                    _tmp = 0
                    stack.pop()
            if _tmp:
                stack.append(_tmp)    
        return stack