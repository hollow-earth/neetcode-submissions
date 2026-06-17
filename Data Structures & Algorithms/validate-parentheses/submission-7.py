class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_dict = {"}":"{", "]": "[", ")":"("}

        for c in s:
            if len(stack) >= 1 and c in valid_dict.keys():
                _c = stack.pop()
                if valid_dict[c] != _c:
                    return False
            else:
                stack.append(c)
        return (len(stack) == 0)