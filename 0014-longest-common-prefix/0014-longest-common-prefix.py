class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 2:
            return self.longestCommonPrefixOfTwo(strs[0], strs[1])
        
        for i in range(len(strs) - 1):
            strs = [self.longestCommonPrefixOfTwo(strs[0], strs[1])] + strs[2:]
        
        return strs[0]
        
    def longestCommonPrefixOfTwo(self, str1: str, str2: str) -> str:
        i = 0
        minLength = min(len(str1), len(str2))
        
        while i < minLength:
            if not str1[i] == str2[i]:
                return str1[:i]
            i += 1
        print(i)
        return str1[:i]