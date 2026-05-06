class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        # This loop must be indented inside the function
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # This loop must also be indented inside the function
        for char in t:
            if char not in count or count[char] == 0:
                return False
            # This must be lined up with the 'if' above it
            count[char] -= 1
            
        # This must be lined up with the 'for' loops
        return True