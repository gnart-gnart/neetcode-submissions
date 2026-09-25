class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_length = 0
        ones = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                ones = 0
            if ones > longest_length:
                longest_length = ones
        return longest_length
        