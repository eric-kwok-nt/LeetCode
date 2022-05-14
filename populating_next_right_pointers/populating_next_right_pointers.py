# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def __init__(self):
        self.queue = []

    def connect(self, root: "Node") -> "Node":
        if root is None:
            return None
        current_idx = 0
        prev_node_idx = None
        previous_level = 0
        root.level = previous_level
        self.queue.append(root)
        while not len(self.queue) == current_idx:
            node = self.queue[current_idx]
            self.current_level = node.level
            if self.current_level > previous_level:
                self.queue[prev_node_idx].next = None
            elif prev_node_idx is not None:
                self.queue[prev_node_idx].next = node

            self.add_node_to_queue(node.left)
            self.add_node_to_queue(node.right)

            previous_level = self.current_level
            prev_node_idx = current_idx
            current_idx += 1
        self.queue[prev_node_idx].next = None
        return root

    def add_node_to_queue(self, children: "Node"):
        if children is not None:
            children.level = self.current_level + 1
            self.queue.append(children)
