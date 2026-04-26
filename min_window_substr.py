#Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring.
#If such a substring does not exist, return an empty string "".
#You may assume that the correct output is always unique.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq, w_freq = {}, {}
        for i in t:
            t_freq[i] = 1 + t_freq.get(i, 0)
        l = 0
        w_count = 0
        t_count = len(t_freq)
        min_l = float("infinity")
        for r in range(len(s)):
            w_freq[s[r]] = 1 + w_freq.get(s[r], 0)
            if s[r] in t_freq and w_freq[s[r]] == t_freq[s[r]]:
                w_count += 1
            while w_count == t_count:
                if r - l + 1 < min_l:
                    min_l = r - l + 1
                    res = (l, r)
                w_freq[s[l]] -= 1
                if s[l] in t_freq and w_freq[s[l]] < t_freq[s[l]]:
                    w_count -= 1
                l += 1
        if min_l == float("infinity"):
            return ""
        return s[res[0] : res[1] + 1]
