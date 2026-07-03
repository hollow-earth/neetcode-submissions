class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        max_length = 0
        l_ptr, r_ptr = 0,0

        if len(s) <= 1:
            return len(s)

        while l_ptr <= r_ptr and r_ptr < len(s):
            if s[r_ptr] not in hs:
                hs.add(s[r_ptr])
                r_ptr += 1
            else:
                hs.remove(s[l_ptr])
                l_ptr += 1
            max_length = max(max_length, r_ptr-l_ptr)
        return max_length
        