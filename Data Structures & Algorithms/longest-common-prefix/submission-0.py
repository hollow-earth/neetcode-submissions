class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_length = min([len(s) for s in strs])
        res = ""
        for i in range(smallest_length):
            c = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != c:
                    return res
            res += c
        return res