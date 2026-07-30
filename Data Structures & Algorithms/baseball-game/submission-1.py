class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for c in operations:
            if c == '+':
                total += stack[-2] + stack[-1]
                stack.append(stack[-2] + stack[-1])
            elif c == 'C':
                total -= stack[-1]
                stack.pop()
            elif c == 'D':
                total += 2 * stack[-1]
                stack.append(2 * stack[-1])
            else:
                total += int(c)
                stack.append(int(c))
        return total