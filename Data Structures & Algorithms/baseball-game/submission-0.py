class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == '+':
                stack.append(int(stack[-2]) + int(stack[-1]))
            elif c == 'C':
                stack.pop()
            elif c == 'D':
                stack.append(2 * int(stack[-1]))
            else:
                stack.append(int(c))
        return sum(stack)