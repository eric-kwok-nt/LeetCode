from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head.next:
            return head
        pos = 1
        curr_node = head
        prev_node = None
        sub_head = None
        sub_head_next = head
        while True:

            if pos == left - 1:
                sub_head = curr_node
                sub_head_next = curr_node.next
                curr_node = curr_node.next

            elif pos > right:
                if sub_head:
                    sub_head.next = prev_node
                else:
                    head = prev_node
                sub_head_next.next = curr_node
                break

            elif pos >= left:
                tmp_prev_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = tmp_prev_node
            else:
                curr_node = curr_node.next
            pos += 1

        return head


# head_list = [1,2,3,4,5]
# left = 2
# right = 4

# head_list = [2]
# left = 1
# right = 1

head_list = [1, 2, 3, 4, 5]
left = 2
right = 5

# head_list = [1,2,3,4,5]
# left = 1
# right = 5


def make_link_list(head_list) -> ListNode:
    head = ListNode(head_list[0])
    node = head
    for idx in range(1, len(head_list)):
        node.next = ListNode(head_list[idx])
        node = node.next
    return head


def print_linked_list(head):
    curr_node = head
    while curr_node:
        print(curr_node.val, end=" ")
        curr_node = curr_node.next
    print()


sol = Solution()
head = make_link_list(head_list)
print(f"Initial linked list: ")
print_linked_list(head)
new_head = sol.reverseBetween(head, left, right)
print(f"New linked list: ")
print_linked_list(new_head)
