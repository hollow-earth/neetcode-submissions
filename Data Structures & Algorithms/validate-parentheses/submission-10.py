class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_c = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if len(stack) >= 1 and c in valid_c.keys():
                if valid_c[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return len(stack) == 0