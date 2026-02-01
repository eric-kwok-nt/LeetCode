from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for character in string:
                arr[ord(character) - ord("a")] += 1
            anagram_dict[tuple(arr)].append(string)
        result = []
        for anagram_group in anagram_dict.values():
            result.append(anagram_group)
        return result
