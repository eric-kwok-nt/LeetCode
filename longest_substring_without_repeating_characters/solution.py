class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        max_length = 0
        start = 0
        for char in s:
            while char in seen:
                seen.remove(s[start])
                start += 1
            seen.add(char)
            if len(seen) > max_length:
                max_length = len(seen)

        return max_length
            