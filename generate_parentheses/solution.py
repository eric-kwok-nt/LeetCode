class Solution:

    def __init__(self):
        self.res = []
        self.n = None

    def generateParenthesis(self, n: int) -> list[str]:
        self.n = n
        self.backtrack([], 0, 0)
        return self.res

    def backtrack(self, cur: list[str], open_used: int, close_used: int):
        if len(cur) == 2 * self.n:
            self.res.append("".join(cur))
            return
        if open_used < self.n:
            cur.append("(")
            self.backtrack(cur, open_used + 1, close_used)
            cur.pop()
        if close_used < open_used:
            cur.append(")")
            self.backtrack(cur, open_used, close_used + 1)
            cur.pop()


if __name__ == "__main__":
    sol = Solution()

    n = 3
    result = sol.generateParenthesis(n)
    print(result)
