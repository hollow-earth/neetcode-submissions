class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()

        while n not in num_set:
            num_set.add(n)
            n = self.sumSquares(n)
            if n == 1:
                return True
        return False



    def sumSquares(self, n: int) -> int:
        _temp = 0
        while n > 0:
            _temp += (n % 10) ** 2
            n = n // 10
        return _temp