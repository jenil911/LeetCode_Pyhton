class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        for r in range(len(s)):
            maxCost -= abs(ord(s[r]) - ord(t[r]))
            if maxCost < 0:
                maxCost += abs(ord(s[l]) - ord(t[l]))
                l += 1

        return r - l + 1