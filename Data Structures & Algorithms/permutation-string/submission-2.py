class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        if len(s1) > len(s2):
            return False
        
        l_ptr, r_ptr = 0, len(s1) - 1
        for i in range(len(s1)):
            s1_freq[ord(s1[i])-97] += 1
            s2_freq[ord(s2[i])-97] += 1
        
        while r_ptr < len(s2) - 1:
            if s1_freq == s2_freq:
                return True
            else:
                s2_freq[ord(s2[l_ptr])-97] -= 1
                l_ptr += 1
                r_ptr += 1
                s2_freq[ord(s2[r_ptr])-97] += 1
                
        return s1_freq == s2_freq