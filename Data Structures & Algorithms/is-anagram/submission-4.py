class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_array, t_array = [0] * 26, [0] * 26

        for i in range(len(s)):
            s_array[ord(s[i])-97] += 1
            t_array[ord(t[i])-97] += 1
        
        return s_array == t_array