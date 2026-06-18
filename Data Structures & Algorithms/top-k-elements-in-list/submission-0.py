from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        res = []
        print(buckets)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

