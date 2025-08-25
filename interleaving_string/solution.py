from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isInterleave(
        self, s1: str, s2: str, s3: str, s1_idx: int = 0, s2_idx: int = 0
    ) -> bool:
        s3_idx = s1_idx + s2_idx
        if len(s1) + len(s2) != len(s3):
            return False
        elif s1_idx == len(s1):
            return s2[s2_idx:] == s3[s3_idx:]
        elif s2_idx == len(s2):
            return s1[s1_idx:] == s3[s3_idx:]
        else:
            if s1[s1_idx] == s3[s3_idx]:
                is_interleave = self.isInterleave(s1, s2, s3, s1_idx + 1, s2_idx)
                if is_interleave:
                    return True
            if s2[s2_idx] == s3[s3_idx]:
                return self.isInterleave(s1, s2, s3, s1_idx, s2_idx + 1)
            return False


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))
