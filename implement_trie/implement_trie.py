from typing import Tuple


class Trie:
    def __init__(self):
        self.tree = [{"$": True}]

    def insert(self, word: str) -> None:
        # write your code here
        current_node = 0
        num_nodes = len(self.tree) - 1
        for currentSymbol in word:
            if currentSymbol in self.tree[current_node]:
                current_node = self.tree[current_node][currentSymbol]
            else:
                num_nodes += 1
                self.tree[current_node].update({currentSymbol: num_nodes})
                current_node = num_nodes
                self.tree.append({})
        self.tree[current_node].update({"$": True})

    def search(self, word: str) -> bool:
        word_present, _ = self._find_word_prefix(word)
        return word_present

    def startsWith(self, prefix: str) -> bool:
        _, prefix_present = self._find_word_prefix(prefix)
        return prefix_present

    def _find_word_prefix(self, string: str) -> Tuple[bool, bool]:
        current_node = 0
        prefix_present = True
        word_present = False
        try:
            for char in string:
                current_node = self.tree[current_node][char]
        except KeyError:
            prefix_present = False
            return word_present, prefix_present
        try:
            word_present = self.tree[current_node]["$"]
            return word_present, prefix_present
        except KeyError:
            prefix_present = True
            return word_present, prefix_present


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    trie.insert("add")
    assert not trie.search("ad")
