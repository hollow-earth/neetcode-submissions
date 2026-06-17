class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        res_list = []
        for i in nums:
            res[i] += 1
        res = sorted([(value,key) for key, value in res.items()], reverse=True)
        for i in range(0,k):
            print(res)
            res_list.append(res[i][1])
        return res_list