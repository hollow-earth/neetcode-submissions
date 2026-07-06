class Solution:
    def mySqrt(self, x: int) -> int:
        _x = x
        while (_x * _x > x):
            _x = (_x + x / _x) // 2
        return int(_x)