class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i, n in enumerate (nums):
            diff = target - n
            if diff in memory:
                return [memory[diff], i]
            memory[n] = i
