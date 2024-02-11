class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        mp = {}
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans
