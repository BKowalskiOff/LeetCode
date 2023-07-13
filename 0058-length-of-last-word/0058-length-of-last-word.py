class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        j = i - 1
        while not s[j] == ' ' and j >= 0:
            j -= 1
        
        return i-j