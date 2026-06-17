class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            _freq = [0] * 26
            for c in s:
                _freq[ord(c) - ord("a")] += 1
            res[tuple(_freq)].append(s)
        return list(res.values())