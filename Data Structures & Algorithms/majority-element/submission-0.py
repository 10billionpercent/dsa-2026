class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        res = 0
        max_count = 0
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            if max_count < counts[i]:
                res = i
                max_count = counts[i]
        return res