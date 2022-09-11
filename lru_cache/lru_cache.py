from typing import List


class Node:
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, -1)
        self.tail = Node(0, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def get(self, key: int) -> int:
        try:
            CurrentNode = self.hashmap[key]
            self._prioritize_node(CurrentNode)
            return CurrentNode.val
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            NewNode = Node(key, value)
            self.hashmap[key] = NewNode
            self._add_node(NewNode)
            if len(self.hashmap) > self.capacity:
                self._evict_old_node()
        else:
            CurrentNode = self.hashmap[key]
            CurrentNode.val = value
            self._prioritize_node(CurrentNode)

    def _evict_old_node(self) -> None:
        node_to_evict = self.tail.prev
        self._remove_node(node_to_evict)
        self.hashmap.pop(node_to_evict.key)
        del node_to_evict

    def _prioritize_node(self, node: Node) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _add_node(self, node: Node) -> None:
        old_front = self.head.next
        old_front.prev = node
        node.next = old_front
        node.prev = self.head
        self.head.next = node

    def _remove_node(self, node_to_remove: Node) -> None:
        p = node_to_remove.prev
        n = node_to_remove.next
        p.next = n
        n.prev = p


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def run_test(sequence: List[str], inputs: List[List[int]]) -> List[int]:
    results = []
    for action, inp in zip(sequence, inputs):
        if action == "LRUCache":
            obj = LRUCache(*inp)
            results.append(None)
        elif action == "put":
            obj.put(*inp)
            results.append(None)
        elif action == "get":
            results.append(obj.get(*inp))
        else:
            print("Wrong action type!")
            raise TypeError
    return results


def main():
    sequence_1 = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    inputs_1 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    sequence_2 = ["LRUCache", "put", "get"]
    inputs_2 = [[1], [2, 1], [2]]

    print(run_test(sequence_1, inputs_1))
    print(run_test(sequence_2, inputs_2))


if __name__ == "__main__":
    main()
