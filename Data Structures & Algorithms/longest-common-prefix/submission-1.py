class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(min(strs))):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return res
            res += char

        return res