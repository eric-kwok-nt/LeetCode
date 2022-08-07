class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.string = s
        self.longest_substring = s[0]
        self.len_longest_substring = 1
        curr_idx = 1
        while curr_idx < len(self.string):
            prev_idx = curr_idx - 1

            next_idx = curr_idx
            to_stop = self.check_longest_substring(prev_idx, next_idx, 0)
            if to_stop:
                break

            next_idx = curr_idx + 1
            to_stop = self.check_longest_substring(prev_idx, next_idx, 1)
            if to_stop:
                break
            curr_idx += 1
        return self.longest_substring

    def check_longest_substring(self, prev_idx, next_idx, init_len):
        while (
            prev_idx >= 0
            and next_idx < len(self.string)
            and self.string[prev_idx] == self.string[next_idx]
        ):
            init_len += 2
            if init_len > self.len_longest_substring:
                self.len_longest_substring = init_len
                self.longest_substring = self.string[prev_idx : next_idx + 1]

            prev_idx -= 1
            next_idx += 1
        if next_idx == len(self.string):
            return True
        return False


if __name__ == "__main__":
    Sol = Solution()
    s = input("Input string:")
    print(Sol.longestPalindrome(s))
