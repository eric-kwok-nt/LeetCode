from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        Result = ListNode()
        CurrResult = Result
        while True:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            val = l1_val + l2_val
            curr_val = val % 10

            curr_result_val = CurrResult.val + curr_val
            CurrResult.val = curr_result_val % 10
            extra_val = curr_result_val // 10 or val // 10
            if not extra_val and (l1 is None) and (l2 is None):
                return Result
            NextResult = ListNode(val=extra_val)
            CurrResult.next = NextResult

            CurrResult = NextResult


def create_linked_list(arr: list):
    Output = ListNode()
    CurrNode = Output
    idx = 0
    while idx < len(arr):
        CurrNode.val = arr[idx]
        if idx < len(arr) - 1:
            CurrNode.next = ListNode()
            CurrNode = CurrNode.next
        idx += 1
    return Output


if __name__ == "__main__":
    # arr1 = [2, 4, 3]
    # arr2 = [5, 6, 4]
    arr1 = [9, 9, 9, 9, 9, 9, 9]
    arr2 = [9, 9, 9, 9]
    # arr1 = [0]
    # arr2 = [0]
    l1 = create_linked_list(arr1)
    l2 = create_linked_list(arr2)

    Sol = Solution()
    result = Sol.addTwoNumbers(l1, l2)
    result_list = []
    while True:
        result_list.append(result.val)
        if result.next is not None:
            result = result.next
        else:
            print(result_list)
            break
