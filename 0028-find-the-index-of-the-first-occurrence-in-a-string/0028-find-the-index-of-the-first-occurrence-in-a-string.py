class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        l1 = len(haystack)
        l2 = len(needle)
        while i < l1:
            print(i,haystack[i])
            while j < l2 and i+j < l1:
                if haystack[i+j] != needle[j]:
                    break
                j += 1
                if j == l2:
                    return i
            i = i+1
            j = 0
        return -1