class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        sum = 0
        for i in range(len(s)-1, -1, -1):
            if i + 1 < len(s):
                if m[s[i+1]] > m[s[i]]:
                    sum -= m[s[i]]
                    continue
            sum += m[s[i]]
        return sum