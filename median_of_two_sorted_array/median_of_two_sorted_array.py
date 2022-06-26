from typing import List


# Solution from https://www.youtube.com/watch?v=q6IEA26hvXc
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len_total = len(nums1) + len(nums2)
        len_half = (len_total) // 2
        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = len_half - 2 - i
            nums1_left = nums1[i] if i >= 0 else float("-infinity")
            nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            nums2_left = nums2[j] if j >= 0 else float("-infinity")
            nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if len_total & 1:  # If odd number of elements
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            if nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    Sol = Solution()
    print(Sol.findMedianSortedArrays(nums1, nums2))
