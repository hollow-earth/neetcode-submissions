class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            char_freq = [0] * 26
            for char in s:
                char_freq[ord(char) - 97] += 1
            hm[tuple(char_freq)].append(s)
        return list(hm.values())
                