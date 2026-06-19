class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = [1]
        right = [1]
        rev = nums[::-1]
        for i in range(1, len(nums)):
            left.append(left[i-1]*nums[i-1])
            right.append(right[i-1]*rev[i-1])
        right.reverse()
        for num in range(len(nums)):
            output.append(left[num]*right[num])
        return output
                

        