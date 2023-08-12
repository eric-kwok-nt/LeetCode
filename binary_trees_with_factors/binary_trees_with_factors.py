from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        num_trees = {k: 1 for k in arr}
        largest_possible_quotient = arr[-1] // arr[0]

        i = 0
        while arr[i] <= largest_possible_quotient:
            j = 0
            while j <= i:
                product = arr[i] * arr[j]
                if product > arr[-1]:
                    break
                elif product in num_trees:
                    if i == j:
                        num_trees[product] += num_trees[arr[i]] * num_trees[arr[j]]
                    else:
                        num_trees[product] += num_trees[arr[i]] * num_trees[arr[j]] * 2
                j += 1
            i += 1
        return sum(num_trees.values()) % (10 ** 9 + 7)


if __name__ == "__main__":
    Sol = Solution()
    # arr = [2, 4, 5, 10]
    # arr = [2, 4]
    arr = [18, 3, 6, 2]
    print(Sol.numFactoredBinaryTrees(arr))
