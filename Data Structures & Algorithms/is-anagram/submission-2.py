class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_to_match1 = list()
        for char in s:
            chars_to_match1 += char
        
        chars_to_match2 = list()
        for char in t:
            chars_to_match2 += char
    
        if sorted(chars_to_match1) == sorted(chars_to_match2):
            return True

        return False