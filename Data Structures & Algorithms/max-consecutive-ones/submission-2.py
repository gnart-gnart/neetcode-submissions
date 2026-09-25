class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
            result = max(count, result)
        return result