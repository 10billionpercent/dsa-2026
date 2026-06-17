class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)+ 1):
            diff = target - nums[i]
            if seen and diff in nums and nums.index(diff) != i:
                return sorted([i, nums.index(diff)])
            else:
                seen[i] = nums[i]
        