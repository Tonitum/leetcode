class Solution(object):
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = (m + n ) - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int):
        insert_index = m - 1
        for num in nums2:
            insert_index = insert_index + 1
            nums1[insert_index] =  num

        # this operation is o(n log n)
        nums1.sort()

