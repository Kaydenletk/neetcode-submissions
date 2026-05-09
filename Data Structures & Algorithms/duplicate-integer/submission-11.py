class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen: #if seen num in folder
                return True
            seen.add(num) #keep adding num in the folder
        return False #return False when dont see any