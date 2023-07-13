class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l = 0
        seen = {s[0]:0}
        res = 1
        
        for r in range(1, len(s)):

            if s[r] in seen:
                if seen[s[r]] < l:
                    seen[s[r]] = r
                    res = max(res, r - l + 1)
                    continue
                
                res = max(res, r - l)
                l = seen[s[r]] + 1
                seen[s[r]] = r
                continue

            seen[s[r]] = r
            res = max(res,r - l + 1)

        return res