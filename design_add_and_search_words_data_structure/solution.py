WILDCARD = "."


class END:
    pass


class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        self.trie[word[0]] = self.trie.get(word[0], {})
        curr_node = self.trie[word[0]]
        for char in word[1:]:
            curr_node[char] = curr_node.get(char, {})
            curr_node = curr_node[char]
        curr_node[END] = {}

    def search(self, word: str) -> bool:
        return self._search_recursive(word, 0, self.trie)

    def _search_recursive(self, word: str, idx: int, curr_node: dict) -> bool:
        if idx == len(word):
            return END in curr_node
        char = word[idx]
        if char in curr_node:
            next_node = curr_node[char]
            return self._search_recursive(word, idx + 1, next_node)
        elif char == WILDCARD:
            is_found = False
            for key, next_node in curr_node.items():
                if key != END:
                    is_found = self._search_recursive(word, idx + 1, next_node)
                    if is_found:
                        return is_found
            return is_found
        else:
            return False


word = "bad"
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word)
print(param_2)
